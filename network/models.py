from django.db import models
from datetime import datetime
from auth.models import ActiveVoter
import hashlib
import random
import secrets
import time
import json


class Transaction(models.Model):
    transaction_id = models.CharField(max_length=100, primary_key=True)
    voter_id = models.CharField(max_length=100)
    salt = models.CharField(max_length=100)
    candidate_hash = models.CharField(max_length=100)

    def createNewTransaction(self, voter_id, candidateId):
        self.transaction_id = secrets.token_hex(10)
        self.voter_id = voter_id
        self.salt = secrets.token_hex(5)
        self.calculateCandidateHash(candidateId)

    def calculateCandidateHash(self, candidateId):
        sha = hashlib.sha256()
        data = candidateId + str(self.salt)
        sha.update(data.encode('utf-8'))
        self.candidate_hash = sha.hexdigest()

    def __str__(self):
        return str(self.voter_id) + '--' + str(self.candidate_hash)


class Block(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    transaction_id = models.CharField(max_length=100)
    prev_hash = models.CharField(max_length=100)
    hash = models.CharField(max_length=100)

    def __str__(self):
        return str(self.hash)

    def createNewBlock(self, transactionId, prevBlock):
        self.timestamp = datetime.now()
        self.transaction_id = transactionId
        self.prev_hash = prevBlock.hash
        self.nonce = 0
        self.difficulty = 4
        self.hash = self.generateHash()
        self.mineBlock()
        return self

    def generateHash(self):
        sha = hashlib.sha256()
        data = str(self.timestamp) + str(self.prev_hash) + str(self.transaction_id) + str(self.nonce)
        sha.update(data.encode('utf-8'))
        return sha.hexdigest()
        
    def selectMiningBlock(self):
        blocks = Block.objects.filter()
        t = []
        for i in blocks:
            t0 = time.time()
            for j in range(0,1000000):
                string = "Hello" + str(j)
                hsh = hashlib.sha256(string).hexdigest()
                if(hsh[:10]=="0000000000"):
                    t.append(time.time() - t0)
        miner = blocks[0]
        for i in range(1, len(t)):
            if(t[i]<t[i-1]):
                miner = blocks[i]
        return miner
    
    def validate_new_block(self):
        verifi = []
        blocks = Block.objects.filter()
        for i in blocks:
            guess = f'{i.hash}{self.hash}'.encode()
            guess_hash = hashlib.sha256(guess).hexdigest()
            if(guess_hash[:4]=="0000"):
                verifi.append('1')
            else:
                verifi.append('2')
        cnt = 0
        total = 0
        for i in verifi:
            total+=1
            if(i=='1'):
                cnt+=1
        if(cnt/total > 0.7):
            return True
        return False

    def mineBlock(self):
        target = str('0' * self.difficulty)
        while str(self.hash)[:self.difficulty] != target:
            self.nonce = self.nonce + 1
            self.hash = self.generateHash()
        print("Block Mined : %s"%(self.hash))


class Peer(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name + "@" + self.address

    def createNewPeer(self, name, address):
        self.id = secrets.token_hex(10)
        self.name = name
        self.address = address
        return self


class Lock(models.Model):
    lock = models.BooleanField(default=False)

    def __str__(self):
        return str(self.lock)





