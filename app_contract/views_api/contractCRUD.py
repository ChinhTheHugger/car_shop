from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from app_contract.models.contract import Contract
from app_contract.serializers.contract import ContractSerializer
import json

class ContractList(APIView):

    # 1. List all
    def get(self, request):
        contracts = Contract.get_all_contracts()
        serializer = ContractSerializer(contracts, many=True)
        
        # this is how you extract data from the api response
        
        # results = Response(serializer.data, status=status.HTTP_200_OK).data
        # print(results)
        # print(results[0])
        # print(results[0]['brand'])
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class ContractCreate(APIView):

    # 2. Create
    def post(self, request, format=None):
        serializer = ContractSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print("Saved")
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ContractGet(APIView):
    
    # 3. Retrieve
    def get(self, request, customerusername):
        contract = Contract.get_contract_by_customer(customerusername)
        serializer = ContractSerializer(contract)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class ContractUpdate(APIView):
    
    # 4. Update
    def put(self, request, customerusername, format=None):
        contract = Contract.get_contract_by_customer(customerusername)
        serializer = ContractSerializer(contract, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, customerusername, format=None):
        contract = Contract.get_contract_by_customer(customerusername)
        serializer = ContractSerializer(contract, request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ContractDelete(APIView):
    
    # 5. Delete
    def delete(self, request, customerusername, car, date):
        contract = Contract.get_contract_by_customer(customerusername)
        serializer = ContractSerializer(contract)
        if serializer.is_valid():
            Contract.delete_contract(customerusername,car,date)
            return Response(status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)