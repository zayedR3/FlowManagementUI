# Corda 5 CorDapp Flow Management Tool


This user guide provides step-by-step instructions on using the Corda 5 flow management tool. This article will help you learn how to connect the running corDapp, make flow calls, configure flow queries, and retrieve results.

## Prerequisites
* Install and run Python and Flask framework. link.

* Prepare your local Corda 5 environment. (By default, the Flow Management Tool is looking to connect to https://localhost:8888/api/v1/swagger#/ with Login: Admin and Password: Admin.)

* Clong the Flow Management Tool repository. FlowManagementUI: main

## Set Up

1. Assuming your local Corda 5 environment is populated and the swagger endpoint is at: https://localhost:8888/api/v1/swagger#/

2. Navigate to where you downloaded the Corda 5 Flow Management Tool

3. To run the framework
   * Navigate to the file name using cd command.
   * use the python app.py command to run it.
     ![image](https://github.com/parisyup/FlowManagementUI/assets/51169685/f0c3bf59-8180-48a0-91cc-80f2d260e530)

   * Later on, click on the IP Address which will open the Interface:

![image](https://github.com/parisyup/FlowManagementUI/assets/51169685/79f58342-ccc3-4135-939c-66a6911e2f20)

The Flow Management Tool should be automatically connected with the CorDapp running locally from your CSDE. You can test the connection by click on the dropdown list at the Flow Initiator section. You should be able to see the vNodes of your started CorDapp from CSDE.

![image](https://github.com/parisyup/FlowManagementUI/assets/51169685/5a2356f2-cd14-489c-abd0-4afe0bf0d251)

## Using the Flow Management Tool

### Selecting the Flow Initiator

As the first step of using the Flow Management Tool, you would need to select the Flow Initiator. The Flow Initiator indicates which vNode will be triggering the flow. If you wish to have Alice to run a transaction to Bob, select the X500Name of Alice. The selected vNode’s shortHash (Corda 5 Network participant identifier) will also be shown below the dropdown list to signify your selection. 

### Function 1: To Make a Flow Call

1. Click on "Flow Call" tab in the application.
2. Paste the your JSON format request body into the request input box.
3. Click Post button to trigger the call.

![image](https://github.com/parisyup/FlowManagementUI/assets/51169685/cac8a516-dfd6-4389-bce5-94ca509c6aa3)

### Function 2: To Configure Flow Query

1. Click on the “Flow Query” tab.
2. Choose whether to query a single flow or all flows at the selected Flow Initiator.
3. If you choose to query all of the flows, select “Query All Flows“ then click “Get“.

![image](https://github.com/parisyup/FlowManagementUI/assets/51169685/0482cfa4-7ee1-42f2-8786-2d8ad80b2936)
4. If you choose to query a single flow, select “Query Single Flow“, please add the ClientID in specified filed.
5. Click on “Get” to retrieve the result.

![image](https://github.com/parisyup/FlowManagementUI/assets/51169685/ed174f78-91f0-4f0a-8fef-d914d8b347ab)
If you have any suggestions or questions, feel free to give us your feedback through Github for a better experience in the future!

## Conclusion
In summary, our project introduces a specialized flow management layer on top of Swagger for Corda developers. We understand the challenges developers face in testing Corda applications due to the complexity of commands, our solution focuses on simplifying the process.

Our all-in-one flow management system provides developers with a unified platform, streamlining development and enhancing efficiency. A key feature allows developers to run flows directly from an externally developed website and monitor their status in real-time, offering a user-friendly and practical solution for Corda developers. Overall, our project aims to make Corda development more accessible and tailored to the specific needs of flow management.

