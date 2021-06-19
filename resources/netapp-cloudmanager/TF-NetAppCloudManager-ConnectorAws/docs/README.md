# TF::NetAppCloudManager::ConnectorAws

Provides a NetApp_CloudManager Connector AWS resource. This can be used to create a new Cloud Manager Connector in AWS.
The environment needs to be configured with the proper credentials before it can be used (aws configure).
The minimum required policy can be found at [Connector deployment policy for AWS](https://s3.amazonaws.com/occm-sample-policies/Policy_for_Setup_As_Service.json)

<!---
i think we need to create section for terraform and point to there
-->

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::NetAppCloudManager::ConnectorAws",
    "Properties" : {
        "<a href="#accountid" title="AccountId">AccountId</a>" : <i>String</i>,
        "<a href="#ami" title="Ami">Ami</a>" : <i>String</i>,
        "<a href="#associatepublicipaddress" title="AssociatePublicIpAddress">AssociatePublicIpAddress</a>" : <i>Boolean</i>,
        "<a href="#company" title="Company">Company</a>" : <i>String</i>,
        "<a href="#enableterminationprotection" title="EnableTerminationProtection">EnableTerminationProtection</a>" : <i>Boolean</i>,
        "<a href="#iaminstanceprofilename" title="IamInstanceProfileName">IamInstanceProfileName</a>" : <i>String</i>,
        "<a href="#instancetype" title="InstanceType">InstanceType</a>" : <i>String</i>,
        "<a href="#keyname" title="KeyName">KeyName</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#proxycertificates" title="ProxyCertificates">ProxyCertificates</a>" : <i>[ String, ... ]</i>,
        "<a href="#proxypassword" title="ProxyPassword">ProxyPassword</a>" : <i>String</i>,
        "<a href="#proxyurl" title="ProxyUrl">ProxyUrl</a>" : <i>String</i>,
        "<a href="#proxyusername" title="ProxyUserName">ProxyUserName</a>" : <i>String</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#securitygroupid" title="SecurityGroupId">SecurityGroupId</a>" : <i>String</i>,
        "<a href="#subnetid" title="SubnetId">SubnetId</a>" : <i>String</i>,
        "<a href="#awstag" title="AwsTag">AwsTag</a>" : <i>[ <a href="awstagdefinition.md">AwsTagDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::NetAppCloudManager::ConnectorAws
Properties:
    <a href="#accountid" title="AccountId">AccountId</a>: <i>String</i>
    <a href="#ami" title="Ami">Ami</a>: <i>String</i>
    <a href="#associatepublicipaddress" title="AssociatePublicIpAddress">AssociatePublicIpAddress</a>: <i>Boolean</i>
    <a href="#company" title="Company">Company</a>: <i>String</i>
    <a href="#enableterminationprotection" title="EnableTerminationProtection">EnableTerminationProtection</a>: <i>Boolean</i>
    <a href="#iaminstanceprofilename" title="IamInstanceProfileName">IamInstanceProfileName</a>: <i>String</i>
    <a href="#instancetype" title="InstanceType">InstanceType</a>: <i>String</i>
    <a href="#keyname" title="KeyName">KeyName</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#proxycertificates" title="ProxyCertificates">ProxyCertificates</a>: <i>
      - String</i>
    <a href="#proxypassword" title="ProxyPassword">ProxyPassword</a>: <i>String</i>
    <a href="#proxyurl" title="ProxyUrl">ProxyUrl</a>: <i>String</i>
    <a href="#proxyusername" title="ProxyUserName">ProxyUserName</a>: <i>String</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#securitygroupid" title="SecurityGroupId">SecurityGroupId</a>: <i>String</i>
    <a href="#subnetid" title="SubnetId">SubnetId</a>: <i>String</i>
    <a href="#awstag" title="AwsTag">AwsTag</a>: <i>
      - <a href="awstagdefinition.md">AwsTagDefinition</a></i>
</pre>

## Properties

#### AccountId

The NetApp account ID that the Connector will be associated with. If not provided, Cloud Manager uses the first account. If no account exists, Cloud Manager creates a new account. You can find the account ID in the account tab of Cloud Manager at [https://cloudmanager.netapp.com](https://cloudmanager.netapp.com).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ami

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AssociatePublicIpAddress

Indicates whether to associate a public IP address to the instance. If not provided, the association will be done based on the subnet's configuration.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Company

The name of the company of the user.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableTerminationProtection

Indicates whether to enable termination protection on the instance, default is false.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IamInstanceProfileName

The name of the instance profile for the Connector.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceType

The type of instance (for example, t3.xlarge). At least 4 CPU and 16 GB of memory are required.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeyName

The name of the key pair to use for the Connector instance.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the Cloud Manager Connector.

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

#### Region

The region where the Cloud Manager Connector will be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityGroupId

The ID of the security group for the instance, multiple security groups can be provided seperated by ','.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubnetId

The ID of the subnet for the instance.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AwsTag

_Required_: No

_Type_: List of <a href="awstagdefinition.md">AwsTagDefinition</a>

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

