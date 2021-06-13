(function(console){

    console.save = function(data, filename){
    
        if(!data) {
            console.error('Console.save: No data')
            return;
        }
    
        if(!filename) filename = 'console.json'
    
        if(typeof data === "object"){
            data = JSON.stringify(data, undefined, 4)
        }
    
        var blob = new Blob([data], {type: 'text/json'}),
            e    = document.createEvent('MouseEvents'),
            a    = document.createElement('a')
    
        a.download = filename
        a.href = window.URL.createObjectURL(blob)
        a.dataset.downloadurl =  ['text/json', a.download, a.href].join(':')
        e.initMouseEvent('click', true, false, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null)
        a.dispatchEvent(e)
     }
    })(console)

classes = temp1
// console.save(classes, "ClassesFromMatrix.json")

classes2 = []

for (var i = 0; i < classes.length; i++){
    if(classes[i].typeOfSession == "ClassSession" ){
        classes2.push( {
            className: classes[i].className,
            sessionCount: classes[i].session.sessionCount,
            studentName: classes[i].studentName,
            teacherName: classes[i].teacherName,
            curriculumLevel: classes[i].session.curriculumLevel,
            sessionNumber: classes[i].sessionNumber,
        } )
    }
}

var cleaned_classes = classes2.filter((a_class, index, self) =>
index === self.findIndex((t) => (t.className === a_class.className && t.studentName === a_class.studentName)))

console.save(cleaned_classes, "CleanedClassesFromMatrix.json")


// --------------------------------------------- //

{
    "kind": 1,
    "id": "756c4757-2167-4ec3-8b17-492836ecb08c",
    "locked": false,
    "lockedDate": null,
    "dayOfWeek": 2,
    "startTime": "2021-05-11T14:30:00.000Z",
    "endTime": "2021-05-11T15:30:00.000Z",
    "newStartTime": "1753-01-01T04:56:02.000Z",
    "newEndTime": "1753-01-01T04:56:02.000Z",
    "allDay": false,
    "recurrence": false,
    "referenceNumber": "V0dsdWchw06LF0koNuywjA",
    "startTimeZone": "UTC -04:00",
    "endTimeZone": "UTC -04:00",
    "classSessionStatus": 1,
    "resources": [],
    "status": 2,
    "substituteStatus": 1,
    "rescheduleCount": 0,
    "expirationDate": null,
    "blockingMode": 0,
    "nextInDateRecurrence": "2021-05-12T13:30:00-04:00",
    "billableStatus": 1,
    "appointmentStyle": 3,
    "availabilityStyle": 0,
    "teachersId": "fc9bd084-a50e-478e-b6f0-f347d18e0bff",
    "studentsId": "783a95b0-fa51-56c0-8910-6cb341e50f10",
    "teacherName": "Chris Schneider",
    "studentName": "Jetta Bernardin",
    "className": "High School Elective Semester 2",
    "typeOfSession": "ClassSession",
    "customStyle": "tentative",
    "customAvailabilityStyle": "unspecified",
    "customEventStyle": "gray",
    "overlapsAnotherInstanceStudent": true,
    "overlapsAnotherInstanceTimeSlot": true,
    "overlapsAnotherInstanceUser": true,
    "overlapsAnotherInstanceTimeSlotRangeAndUser": false,
    "overlapsAnotherInstanceTimeSlotRangeAndStudent": false,
    "isRemote": false,
    "teacher": {},
    "student": {},
    "session": {},
    "isSessionStatusSet": false,
    "classroom": {},
    "users": [],
    "students": [],
    "series": {},
    "sessionNumber": 4,
    "deliveryMethod": {},
    "reservationInstanceType": 0,
    "isVirtualSession": false,
    "isCancelledSession": false,
    "lastUpdated": "2021-05-03T15:23:26.4506659+00:00",
    "updatedBy": "Sync Job"
  }



//--------------------------------------

{
    "kind": 1,
    "id": "756c4757-2167-4ec3-8b17-492836ecb08c",
    "locked": false,
    "lockedDate": null,
    "dayOfWeek": 2,
    "startTime": "2021-05-11T14:30:00.000Z",
    "endTime": "2021-05-11T15:30:00.000Z",
    "newStartTime": "1753-01-01T04:56:02.000Z",
    "newEndTime": "1753-01-01T04:56:02.000Z",
    "allDay": false,
    "recurrence": false,
    "referenceNumber": "V0dsdWchw06LF0koNuywjA",
    "startTimeZone": "UTC -04:00",
    "endTimeZone": "UTC -04:00",
    "classSessionStatus": 1,
    "resources": [],
    "status": 2,
    "substituteStatus": 1,
    "rescheduleCount": 0,
    "expirationDate": null,
    "blockingMode": 0,
    "nextInDateRecurrence": "2021-05-12T13:30:00-04:00",
    "billableStatus": 1,
    "appointmentStyle": 3,
    "availabilityStyle": 0,
    "teachersId": "fc9bd084-a50e-478e-b6f0-f347d18e0bff",
    "studentsId": "783a95b0-fa51-56c0-8910-6cb341e50f10",
    "teacherName": "Chris Schneider",
    "studentName": "Jetta Bernardin",
    "className": "High School Elective Semester 2",
    "typeOfSession": "ClassSession",
    "customStyle": "tentative",
    "customAvailabilityStyle": "unspecified",
    "customEventStyle": "gray",
    "overlapsAnotherInstanceStudent": true,
    "overlapsAnotherInstanceTimeSlot": true,
    "overlapsAnotherInstanceUser": true,
    "overlapsAnotherInstanceTimeSlotRangeAndUser": false,
    "overlapsAnotherInstanceTimeSlotRangeAndStudent": false,
    "isRemote": false,
    "teacher": {
      "modelKey": 1892,
      "hashKey": "fc9bd084-a50e-478e-b6f0-f347d18e0bff",
      "employeeId": 101558,
      "firstName": "Chris",
      "lastName": "Schneider",
      "contacts": [
        {
          "modelKey": 0,
          "hashKey": "00000000-0000-0000-0000-000000000000",
          "userKey": 0,
          "contact": {
            "modelKey": 0,
            "hashKey": "00000000-0000-0000-0000-000000000000",
            "type": 1,
            "firstName": "",
            "lastName": "",
            "email": "",
            "phoneNumbers": [],
            "addresses": []
          }
        },
        {
          "modelKey": 0,
          "hashKey": "00000000-0000-0000-0000-000000000000",
          "userKey": 0,
          "contact": {
            "modelKey": 0,
            "hashKey": "00000000-0000-0000-0000-000000000000",
            "type": 2,
            "firstName": "",
            "lastName": "",
            "email": "",
            "phoneNumbers": [],
            "addresses": []
          }
        }
      ],
      "campuses": [],
      "departments": [],
      "payCodes": [],
      "teachableClasses": [],
      "educationLevels": [],
      "availability": {},
      "nameOverride": "",
      "active": true,
      "hasPhoto": false,
      "hasMealBreakWaiver": false,
      "iana": null,
      "contactSelf": {
        "modelKey": 0,
        "hashKey": "00000000-0000-0000-0000-000000000000",
        "userKey": 0,
        "contact": {
          "modelKey": 0,
          "hashKey": "00000000-0000-0000-0000-000000000000",
          "type": 1,
          "firstName": "",
          "lastName": "",
          "email": "",
          "phoneNumbers": [],
          "addresses": []
        }
      },
      "emergencyContact": {
        "modelKey": 0,
        "hashKey": "00000000-0000-0000-0000-000000000000",
        "userKey": 0,
        "contact": {
          "modelKey": 0,
          "hashKey": "00000000-0000-0000-0000-000000000000",
          "type": 2,
          "firstName": "",
          "lastName": "",
          "email": "",
          "phoneNumbers": [],
          "addresses": []
        }
      }
    },
    "student": {
      "modelKey": 26276,
      "hashKey": "783a95b0-fa51-56c0-8910-6cb341e50f10",
      "studentId": "120010127023",
      "firstName": "Jetta",
      "lastName": "Bernardin",
      "hasPhoto": false,
      "campuses": [],
      "studentStatus": 1,
      "gradeLevel": "11",
      "studentType": 2,
      "contacts": [
        {
          "modelKey": 0,
          "hashKey": "00000000-0000-0000-0000-000000000000",
          "studentKey": 0,
          "contact": {
            "modelKey": 0,
            "hashKey": "00000000-0000-0000-0000-000000000000",
            "type": 0,
            "firstName": "",
            "lastName": "",
            "email": "",
            "phoneNumbers": [],
            "addresses": []
          }
        }
      ],
      "notes": [],
      "iana": "America/New_York",
      "contactSelf": {
        "modelKey": 0,
        "hashKey": "00000000-0000-0000-0000-000000000000",
        "studentKey": 0,
        "contact": {
          "modelKey": 0,
          "hashKey": "00000000-0000-0000-0000-000000000000",
          "type": 0,
          "firstName": "",
          "lastName": "",
          "email": "",
          "phoneNumbers": [],
          "addresses": []
        }
      },
      "defaultCampus": {
        "modelKey": 0,
        "hashKey": "00000000-0000-0000-0000-000000000000",
        "studentKey": 0,
        "campus": {
          "modelKey": 0,
          "hashKey": "00000000-0000-0000-0000-000000000000",
          "name": "",
          "iana": "",
          "timeZoneOffset": "",
          "timeZoneInfoId": "",
          "settings": {
            "modelKey": 0,
            "hashKey": "00000000-0000-0000-0000-000000000000",
            "businessHours": [],
            "allowedHoldsPerStudent": 0,
            "repeatConfigurations": [],
            "planningTimeRestrictionOverride": false,
            "enableClassroomConflictCheck": false
          },
          "priceLists": []
        }
      },
      "contracts": [],
      "authorizedClassTypes": [],
      "startDate": "1753-01-01T07:00:00+00:00"
    },
    "session": {
      "contractHashKey": "3df61092-6128-5780-bf28-3d3c0c41f70d",
      "classType": {
        "name": "High School Elective",
        "department": {
          "name": "Electives",
          "modelKey": 6,
          "hashKey": "08da4551-d7e2-52ed-8c6a-6da556b199a9",
          "created": "0001-01-01T00:00:00+00:00"
        },
        "isTutoring": false,
        "isMastery": false,
        "hasHonors": false,
        "code": "HSELECB",
        "modelKey": 400,
        "hashKey": "800030e7-1654-51cb-bd1b-fefcc411d22f",
        "created": "0001-01-01T00:00:00+00:00"
      },
      "sessionCount": 25,
      "contractedSessionCount": 0,
      "sessionCountBooked": 25,
      "sessionCountTaken": 0,
      "actualNumberOfCurrentlyScheduledSessions": 25,
      "unitPrice": 176.8,
      "totalPrice": 4420,
      "courseMap": "Standard",
      "curriculumLevel": "One Level",
      "semester": 0,
      "name": "High School Elective Semester 2",
      "isMastery": false,
      "isTutoring": false,
      "isDeleted": false,
      "contract": {
        "contractNumber": "0391441",
        "enrollmentYear": 2020,
        "enrollmentYearStart": 2020,
        "enrollmentYearEnd": 2021,
        "isBilled": true,
        "isPaid": false,
        "isTerminated": false,
        "isDeleted": false,
        "modelKey": 191396,
        "hashKey": "3df61092-6128-5780-bf28-3d3c0c41f70d",
        "created": "0001-01-01T00:00:00+00:00"
      },
      "sessionType": 1,
      "isGroupClass": false,
      "description": "Economics",
      "modelKey": 777496,
      "hashKey": "f41dfd6e-ae93-5c0b-a366-a5479e488f1b",
      "created": "0001-01-01T00:00:00+00:00"
    },
    "isSessionStatusSet": false,
    "classroom": {
      "modelKey": 0,
      "hashKey": "00000000-0000-0000-0000-000000000000",
      "name": "",
      "campus": {
        "modelKey": 0,
        "hashKey": "00000000-0000-0000-0000-000000000000",
        "name": "",
        "iana": "",
        "timeZoneOffset": "",
        "timeZoneInfoId": "",
        "settings": {
          "modelKey": 0,
          "hashKey": "00000000-0000-0000-0000-000000000000",
          "businessHours": [],
          "allowedHoldsPerStudent": 0,
          "repeatConfigurations": [],
          "planningTimeRestrictionOverride": false,
          "enableClassroomConflictCheck": false
        },
        "priceLists": []
      },
      "displayOrder": 0
    },
    "users": [
      {
        "modelKey": 11873225,
        "hashKey": "2568af8e-4137-40fc-9650-cde0dade2ec2",
        "user": {
          "modelKey": 1892,
          "hashKey": "fc9bd084-a50e-478e-b6f0-f347d18e0bff",
          "employeeId": 101558,
          "firstName": "Chris",
          "lastName": "Schneider",
          "contacts": [
            {
              "modelKey": 0,
              "hashKey": "00000000-0000-0000-0000-000000000000",
              "userKey": 0,
              "contact": {
                "modelKey": 0,
                "hashKey": "00000000-0000-0000-0000-000000000000",
                "type": 1,
                "firstName": "",
                "lastName": "",
                "email": "",
                "phoneNumbers": [],
                "addresses": []
              }
            },
            {
              "modelKey": 0,
              "hashKey": "00000000-0000-0000-0000-000000000000",
              "userKey": 0,
              "contact": {
                "modelKey": 0,
                "hashKey": "00000000-0000-0000-0000-000000000000",
                "type": 2,
                "firstName": "",
                "lastName": "",
                "email": "",
                "phoneNumbers": [],
                "addresses": []
              }
            }
          ],
          "campuses": [],
          "departments": [],
          "payCodes": [],
          "teachableClasses": [],
          "educationLevels": [],
          "availability": {},
          "nameOverride": "",
          "active": true,
          "hasPhoto": false,
          "hasMealBreakWaiver": false,
          "iana": null,
          "contactSelf": {
            "modelKey": 0,
            "hashKey": "00000000-0000-0000-0000-000000000000",
            "userKey": 0,
            "contact": {
              "modelKey": 0,
              "hashKey": "00000000-0000-0000-0000-000000000000",
              "type": 1,
              "firstName": "",
              "lastName": "",
              "email": "",
              "phoneNumbers": [],
              "addresses": []
            }
          },
          "emergencyContact": {
            "modelKey": 0,
            "hashKey": "00000000-0000-0000-0000-000000000000",
            "userKey": 0,
            "contact": {
              "modelKey": 0,
              "hashKey": "00000000-0000-0000-0000-000000000000",
              "type": 2,
              "firstName": "",
              "lastName": "",
              "email": "",
              "phoneNumbers": [],
              "addresses": []
            }
          }
        },
        "level": 3,
        "type": 2,
        "payCode": {
          "code": "W",
          "description": "Wage",
          "regularTime": "E 1",
          "overTime": "EWO",
          "doubleOverTime": "E 3",
          "discretionary": false,
          "adminOnlyDiscretionary": false,
          "isPlanning": false,
          "isTraining": false,
          "isStudentEvent": false,
          "isHomeworkCafe": false,
          "isMiscellaneousUnpaidEvent": false,
          "isUnpaidTimeOff": false,
          "groupAllowed": false,
          "recurrenceAllowed": false,
          "studentsAllowed": true,
          "paidTimeOff": false,
          "classroomRequired": true,
          "isActive": true,
          "type": 1,
          "isAutoAssigned": true,
          "modelKey": 1,
          "hashKey": "cf5910ff-53a9-4a0b-af38-d5ea27e8a475",
          "created": "0001-01-01T00:00:00+00:00"
        },
        "isSubstitute": false
      }
    ],
    "students": [
      {
        "modelKey": 11873225,
        "hashKey": "38358507-f514-4599-88f4-1318f7ab51c8",
        "student": {
          "modelKey": 26276,
          "hashKey": "783a95b0-fa51-56c0-8910-6cb341e50f10",
          "studentId": "120010127023",
          "firstName": "Jetta",
          "lastName": "Bernardin",
          "hasPhoto": false,
          "campuses": [],
          "studentStatus": 1,
          "gradeLevel": "11",
          "studentType": 2,
          "contacts": [
            {
              "modelKey": 0,
              "hashKey": "00000000-0000-0000-0000-000000000000",
              "studentKey": 0,
              "contact": {
                "modelKey": 0,
                "hashKey": "00000000-0000-0000-0000-000000000000",
                "type": 0,
                "firstName": "",
                "lastName": "",
                "email": "",
                "phoneNumbers": [],
                "addresses": []
              }
            }
          ],
          "notes": [],
          "iana": "America/New_York",
          "contactSelf": {
            "modelKey": 0,
            "hashKey": "00000000-0000-0000-0000-000000000000",
            "studentKey": 0,
            "contact": {
              "modelKey": 0,
              "hashKey": "00000000-0000-0000-0000-000000000000",
              "type": 0,
              "firstName": "",
              "lastName": "",
              "email": "",
              "phoneNumbers": [],
              "addresses": []
            }
          },
          "defaultCampus": {
            "modelKey": 0,
            "hashKey": "00000000-0000-0000-0000-000000000000",
            "studentKey": 0,
            "campus": {
              "modelKey": 0,
              "hashKey": "00000000-0000-0000-0000-000000000000",
              "name": "",
              "iana": "",
              "timeZoneOffset": "",
              "timeZoneInfoId": "",
              "settings": {
                "modelKey": 0,
                "hashKey": "00000000-0000-0000-0000-000000000000",
                "businessHours": [],
                "allowedHoldsPerStudent": 0,
                "repeatConfigurations": [],
                "planningTimeRestrictionOverride": false,
                "enableClassroomConflictCheck": false
              },
              "priceLists": []
            }
          },
          "contracts": [],
          "authorizedClassTypes": [],
          "startDate": "1753-01-01T07:00:00+00:00"
        },
        "level": 3,
        "type": 3
      }
    ],
    "series": {
      "allowParticipation": false,
      "allowAnonymousParticipation": false,
      "status": 1,
      "instances": [],
      "reminders": [],
      "type": 1,
      "blockingMode": 5,
      "kind": 1,
      "title": "High School Elective Semester 2 with Jetta Bernardin",
      "repeatType": 2,
      "repeatConfiguration": "interval=1|termination=2021-06-24T15:30:00.0000000+00:00|days=Tuesday,Thursday",
      "startTimeZone": "Eastern Standard Time",
      "endTimeZone": "Eastern Standard Time",
      "allDay": false,
      "recurrence": true,
      "description": "High School Elective Semester 2 with Jetta Bernardin",
      "payCode": {
        "code": "W",
        "description": "Wage",
        "regularTime": "E 1",
        "overTime": "EWO",
        "doubleOverTime": "E 3",
        "discretionary": false,
        "adminOnlyDiscretionary": false,
        "isPlanning": false,
        "isTraining": false,
        "isStudentEvent": false,
        "isHomeworkCafe": false,
        "isMiscellaneousUnpaidEvent": false,
        "isUnpaidTimeOff": false,
        "groupAllowed": false,
        "recurrenceAllowed": false,
        "studentsAllowed": true,
        "paidTimeOff": false,
        "classroomRequired": true,
        "isActive": true,
        "type": 1,
        "isAutoAssigned": true,
        "modelKey": 1,
        "hashKey": "cf5910ff-53a9-4a0b-af38-d5ea27e8a475",
        "created": "0001-01-01T00:00:00+00:00"
      },
      "campus": {
        "name": "Fusion Upper West Side",
        "timeZoneOffset": "UTC -04:00",
        "timeZoneInfoId": "Eastern Standard Time",
        "iana": "America/New_York",
        "modelKey": 28,
        "hashKey": "21bf85b0-fe42-5885-aff3-4ca475e05962",
        "created": "0001-01-01T00:00:00+00:00"
      },
      "draft": false,
      "allowOverlap": false,
      "skipNonServiceDays": true,
      "modelKey": 3697138,
      "hashKey": "f296049c-b011-4b38-a283-f63fa51752d8",
      "created": "0001-01-01T00:00:00+00:00"
    },
    "sessionNumber": 4,
    "deliveryMethod": {
      "displayName": "In-Person",
      "value": "In-Person",
      "isDefault": true,
      "canDeactivate": true,
      "modelKey": 1,
      "hashKey": "5340be40-cf13-4ec5-907c-60d70ff64bd0",
      "created": "2019-01-30T19:07:50.01+00:00"
    },
    "reservationInstanceType": 0,
    "isVirtualSession": false,
    "isCancelledSession": false,
    "lastUpdated": "2021-05-03T15:23:26.4506659+00:00",
    "updatedBy": "Sync Job"
  }