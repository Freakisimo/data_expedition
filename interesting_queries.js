// Get total of contracts with status and awardCriteria
db.contrataciones.aggregate(
  [
    {
      $match: {
        "records.compiledRelease.tender.awardCriteria": {$exists: true},
        "records.compiledRelease.tender.status": "complete"
      }
    },
    {
      $group : {
        _id : {
          "awardCriteria":"$records.compiledRelease.tender.awardCriteria",
          "status":"$records.compiledRelease.tender.status",
        },
        count:{$sum:1}}
    }
  ]
)

// Get total of contrats by procurementMethodRationale
db.contrataciones.aggregate(
  [
    {
      $match: {
        "records.compiledRelease.tender.procurementMethodRationale": {$exists: true},
        "records.compiledRelease.tender.status": "complete"
      }
    },
    {
      $group : {
        _id : {
          "procurementMethodRationale":"$records.compiledRelease.tender.procurementMethodRationale"
        },
        count:{$sum:1}}
    }
  ]
)


// get all description from complete contract
db.contrataciones.find({
  "records.compiledRelease.tender.description": {$exists: true},
  "records.compiledRelease.tender.status": "complete"
}, {
  "records.compiledRelease.tender.description":1
})
