rs.initiate({
        _id: "myReplSet",
        configsvr: true,
        members: [ 
            { _id : 0, host : "172.31.24.206:27019"}, 
            { _id : 1, host : "172.31.18.234:27019"},
            { _id : 2, host : "172.31.22.191:27019"}
        ]
    }
)   

cd C:\MyStuff\Courses\nosql 
ssh -i C:\MyStuff\Courses\nosql\kira.pem ubuntu@3.86.59.73

ssh -i C:\MyStuff\Courses\nosql\kira.pem ubuntu@54.90.81.138
ssh -i C:\MyStuff\Courses\nosql\kira.pem ubuntu@107.20.25.74
ssh -i C:\MyStuff\Courses\nosql\kira.pem ubuntu@54.226.254.250

ssh -i C:\MyStuff\Courses\nosql\kira.pem ubuntu@54.161.196.203
ssh -i C:\MyStuff\Courses\nosql\kira.pem ubuntu@34.238.119.7
ssh -i C:\MyStuff\Courses\nosql\kira.pem ubuntu@3.93.23.157

54.91.67.113
54.80.239.239
3.88.90.168

54.175.165.239
54.163.42.15
54.227.125.207

sudo mongod --configsvr --replSet myReplSet --dbpath /data/db --port 27019 --logpath /var/log/mongodb/mongod.log --bind_ip 0.0.0.0 --fork

sudo mkdir -p /data/db0                                                                                                                                                                  sudo chmod 777 /data/db0 
sudo chmod 777 /data/db0 
sudo mongod --shardsvr --replSet "rs0" --dbpath /data/db0 --port 27020 --bind_ip 0.0.0.0
sudo mkdir -p /data/db1
sudo chmod 777 /data/db1
sudo mongod --shardsvr --replSet "rs1" --dbpath /data/db1 --port 27021 --bind_ip 0.0.0.0
sudo mkdir -p /data/db2
sudo chmod 777 /data/db2
sudo mongod --shardsvr --replSet "rs2" --dbpath /data/db2 --port 27022 --bind_ip 0.0.0.0


mongos --configdb myReplSet/172.31.24.206:27019,172.31.18.234:27019,172.31.22.191:27019 --port 27018

rs.initiate(
{
       _id: "rs2",
       version: 1,
       members: [
          { _id: 0, host : "172.31.92.25:27022" },
          { _id: 1, host : "172.31.90.243:27022" },
      { _id: 2, host : "172.31.94.32:27022" }    
       ]
    }
 )

 rs.initiate(
    {
           _id: "rs0",
           version: 1,
           members: [
              { _id: 0, host : "172.31.92.25:27020" },
              { _id: 1, host : "172.31.90.243:27020" },
          { _id: 2, host : "172.31.94.32:27020" }    
           ]
        }
     )

     rs.initiate(
        {
               _id: "rs1",
               version: 1,
               members: [
                  { _id: 0, host : "172.31.92.25:27021" },
                  { _id: 1, host : "172.31.90.243:27021" },
              { _id: 2, host : "172.31.94.32:27021" }    
               ]
            }
         )

sh.addShard("rs0/172.31.92.25:27020,172.31.90.243:27020,172.31.94.32:27020");
sh.addShard("rs1/172.31.92.25:27021,172.31.90.243:27021,172.31.94.32:27021");
sh.addShard("rs2/172.31.92.25:27022,172.31.90.243:27022,172.31.94.32:27022");


docker exec -it mynode bash

mongoimport grades.json -d  students -c grades --port 27018
mongoimport grades.json -d  mydb -c grades
git clone https://github.com/neelabalan/mongodb-sample-dataset.git

sh.enableSharding("students")

sh.shardCollection("students.grades", { "student_id" : "hashed" } )

var start = new Date();db.grades.aggregate([{
    $project: {
        student_id: 1,
        "Class ID Range": { $range: [ 0, "$class_id", 25 ] }
    }
}]); var end = new Date(); 

db.grades.aggregate([{
   $project: {
       student_id: 1,
       "Class ID Range": { $range: [ 0, "$class_id", 25 ] }
   }
}]).explain()


var start = new Date();db.grades.find(
   { scores: { $elemMatch: { type: "exam", score: {$gte: 40, $lt: 85}  } } }
).limit(5); var end = new Date(); 

db.grades.find(
   { scores: { $elemMatch: { type: "exam", score: {$gte: 40, $lt: 85}  } } }
).limit(5).explain()

var start = new Date();db.grades.find( { 
   class_id: { $in: [ 5, 15 ] } 
}).limit(5);var end = new Date(); 


db.grades.find( { 
   class_id: { $in: [ 5, 15 ] } }).explain()

   var start = new Date();db.grades.find( { 
   class_id: { $nin: [ 5, 15 ] } }).limit(5); var end = new Date(); 

db.grades.find( { 
   class_id: { $nin: [ 5, 15 ] } }).explain()

var start = new Date();db.grades.find(
{ scores: {$all:[
   { $elemMatch: { type: "exam", score: {$gte: 40, $lt: 85}  } },
   { $elemMatch: { type: "homework", score: {$gte: 40, $lt: 85}  } } 
]}}).limit(5); var end = new Date(); 

db.grades.find(
   { scores: {$all:[
      { $elemMatch: { type: "exam", score: {$gte: 40, $lt: 85}  } },
      { $elemMatch: { type: "homework", score: {$gte: 40, $lt: 85}  } } 
   ]}}).explain()

var start = new Date();db.grades.aggregate( [ {
   $match: { class_id: 5 }
},{
   $group: { _id: "$student_id" }
}]);var end = new Date(); 

db.grades.aggregate( [ {
   $match: { class_id: 5 }
},{
   $group: { _id: "$student_id" }
}]).explain()

var mapFunction = function(){emit(this.student_id,1)}
var reduceFunction = function(key,values){return Array.sum(values)} 
var start = new Date();db.grades.mapReduce(
   mapFunction, reduceFunction, 
   {'out':'mapReduce_output'});var end = new Date(); 

db.mapReduce_output.find({})
db.grades.explain("executionStats").mapReduce(
   mapFunction, reduceFunction, 
   {'out':'MapReduce_output'})


var start = new Date();db.grades.updateMany({ 
student_id: {$in: [ 4, 5 ]} }, 
{ $set: { Address: { county: "Santa Clara", city: "San Jose" }
}});var end = new Date();   


db.grades.explain("executionStats").updateMany({ 
   student_id: {$in: [ 4, 5 ]} }, 
   { $set: { Address: { county: "Santa Clara", city: "San Jose" }
   }})
db.grades.find({"Address.county": "Santa Clara"}).explain()


git clone https://github.com/sriyabalineni/nosql.git
cd nosql
chmod +x install_mongo.sh 
sudo ./install_mongo.sh
sudo service mongod start 
mongosh

sudo mkdir -p /data/db  
 sudo chmod 777 /data/db 

sudo mongod --configsvr --replSet myReplSet --dbpath /data/db --port 27019 --logpath /var/log/mongodb/mongod.log --bind_ip 0.0.0.0 --fork
ps -aux | grep mongod  
sudo kill -9 
sudo vi /etc/mongod.conf 
sudo mongod --configsvr --replSet myReplSet --dbpath /data/db --port 27019 --logpath /var/log/mongodb/mongod.log --bind_ip 0.0.0.0 --fork

sudo lsof -iTCP -sTCP:LISTEN | grep mongo

 mkdir a0 a1 b0 b1 c0 c1  

sudo mkdir -p /data/db0                                                                                                                                                                  sudo chmod 777 /data/db0 

sudo mongod --shardsvr --replSet "rs0" --dbpath /data/db1 --port 27021 --bind_ip 0.0.0.0


