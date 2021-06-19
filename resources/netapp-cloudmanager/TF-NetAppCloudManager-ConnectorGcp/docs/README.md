# TF::NetAppCloudManager::ConnectorGcp

Provides a NetApp_CloudManager connector GCP resource. This can be used to create a new Cloud Manager Connector in GCP.
In order to use that resource, you should have a service account key file. The minimum required policy can be found here: [Connector deployment policy for GCP](https://occm-sample-policies.s3.amazonaws.com/Setup_As_Service_3.7.3_GCP.yaml).
The service account for the Connector VM instance must have the permissions defined in [Cloud Manager policy for GCP](https://occm-sample-policies.s3.amazonaws.com/Policy_for_Cloud_Manager_3.8.0_GCP.yaml)

<!---
i think we need to create section for terraform and point to there
-->

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::NetAppCloudManager::ConnectorGcp",
    "Properties" : {
        "<a href="#accountid" title="AccountId">AccountId</a>" : <i>String</i>,
        "<a href="#associatepublicip" title="AssociatePublicIp">AssociatePublicIp</a>" : <i>Boolean</i>,
        "<a href="#company" title="Company">Company</a>" : <i>String</i>,
        "<a href="#firewalltags" title="FirewallTags">FirewallTags</a>" : <i>Boolean</i>,
        "<a href="#machinetype" title="MachineType">MachineType</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#networkprojectid" title="NetworkProjectId">NetworkProjectId</a>" : <i>String</i>,
        "<a href="#projectid" title="ProjectId">ProjectId</a>" : <i>String</i>,
        "<a href="#proxycertificates" title="ProxyCertificates">ProxyCertificates</a>" : <i>[ String, ... ]</i>,
        "<a href="#proxypassword" title="ProxyPassword">ProxyPassword</a>" : <i>String</i>,
        "<a href="#proxyurl" title="ProxyUrl">ProxyUrl</a>" : <i>String</i>,
        "<a href="#proxyusername" title="ProxyUserName">ProxyUserName</a>" : <i>String</i>,
        "<a href="#serviceaccountemail" title="ServiceAccountEmail">ServiceAccountEmail</a>" : <i>String</i>,
        "<a href="#serviceaccountpath" title="ServiceAccountPath">ServiceAccountPath</a>" : <i>String</i>,
        "<a href="#subnetid" title="SubnetId">SubnetId</a>" : <i>String</i>,
        "<a href="#zone" title="Zone">Zone</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::NetAppCloudManager::ConnectorGcp
Properties:
    <a href="#accountid" title="AccountId">AccountId</a>: <i>String</i>
    <a href="#associatepublicip" title="AssociatePublicIp">AssociatePublicIp</a>: <i>Boolean</i>
    <a href="#company" title="Company">Company</a>: <i>String</i>
    <a href="#firewalltags" title="FirewallTags">FirewallTags</a>: <i>Boolean</i>
    <a href="#machinetype" title="MachineType">MachineType</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#networkprojectid" title="NetworkProjectId">NetworkProjectId</a>: <i>String</i>
    <a href="#projectid" title="ProjectId">ProjectId</a>: <i>String</i>
    <a href="#proxycertificates" title="ProxyCertificates">ProxyCertificates</a>: <i>
      - String</i>
    <a href="#proxypassword" title="ProxyPassword">ProxyPassword</a>: <i>String</i>
    <a href="#proxyurl" title="ProxyUrl">ProxyUrl</a>: <i>String</i>
    <a href="#proxyusername" title="ProxyUserName">ProxyUserName</a>: <i>String</i>
    <a href="#serviceaccountemail" title="ServiceAccountEmail">ServiceAccountEmail</a>: <i>String</i>
    <a href="#serviceaccountpath" title="ServiceAccountPath">ServiceAccountPath</a>: <i>String</i>
    <a href="#subnetid" title="SubnetId">SubnetId</a>: <i>String</i>
    <a href="#zone" title="Zone">Zone</a>: <i>String</i>
</pre>

## Properties

#### AccountId

The NetApp account ID that the Connector will be associated with. If not provided, Cloud Manager uses the first account. If no account exists, Cloud Manager creates a new account. You can find the account ID in the account tab of Cloud Manager at [https://cloudmanager.netapp.com](https://cloudmanager.netapp.com).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AssociatePublicIp

Indicates whether to associate a public IP address to the virtual machine. The default is "true".

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Company

The name of the company of the user.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FirewallTags

Indicates whether to add firewall_tags to the connector VM (HTTP and HTTP). The default is "true".

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MachineType

The machine_type for the Connector VM. The default value is "n1-standard-4".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the Cloud Manager Connector.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkProjectId

The project id in GCP associated with the Subnet. If not provided, it’s assumed that the Subnet is within the previously specified project id.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProjectId

The GCP project_id where the connector will be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProxyCertificates

The proxy certificates. A list of certificate file names.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProxyPassword

The proxy password, if using a proxy to connect to the internet.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProxyUrl

The proxy URL, if using a proxy to connect to the internet.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProxyUserName

The proxy user name, if using a proxy to connect to the internet.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceAccountEmail

The email of the service_account for the connector instance. This service account is used to allow the Connector to create Cloud Volume ONTAP.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceAccountPath

The local path of the service_account JSON file for GCP authorization purposes. This service account is used to create the Connector in GCP.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubnetId

The name of the subnet for the virtual machine. The default value is "Default".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Zone

The GCP zone where the Connector will be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### ClientId

Returns the <code>ClientId</code> value.

#### Id

Returns the <code>Id</code> value.

