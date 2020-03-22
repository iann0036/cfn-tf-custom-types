# Terraform::AWS::OpsworksStack

CloudFormation equivalent of aws_opsworks_stack

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::OpsworksStack",
    "Properties" : {
        "<a href="#agentversion" title="AgentVersion">AgentVersion</a>" : <i>String</i>,
        "<a href="#berkshelfversion" title="BerkshelfVersion">BerkshelfVersion</a>" : <i>String</i>,
        "<a href="#color" title="Color">Color</a>" : <i>String</i>,
        "<a href="#configurationmanagername" title="ConfigurationManagerName">ConfigurationManagerName</a>" : <i>String</i>,
        "<a href="#configurationmanagerversion" title="ConfigurationManagerVersion">ConfigurationManagerVersion</a>" : <i>String</i>,
        "<a href="#customjson" title="CustomJson">CustomJson</a>" : <i>String</i>,
        "<a href="#defaultavailabilityzone" title="DefaultAvailabilityZone">DefaultAvailabilityZone</a>" : <i>String</i>,
        "<a href="#defaultinstanceprofilearn" title="DefaultInstanceProfileArn">DefaultInstanceProfileArn</a>" : <i>String</i>,
        "<a href="#defaultos" title="DefaultOs">DefaultOs</a>" : <i>String</i>,
        "<a href="#defaultrootdevicetype" title="DefaultRootDeviceType">DefaultRootDeviceType</a>" : <i>String</i>,
        "<a href="#defaultsshkeyname" title="DefaultSshKeyName">DefaultSshKeyName</a>" : <i>String</i>,
        "<a href="#defaultsubnetid" title="DefaultSubnetId">DefaultSubnetId</a>" : <i>String</i>,
        "<a href="#hostnametheme" title="HostnameTheme">HostnameTheme</a>" : <i>String</i>,
        "<a href="#manageberkshelf" title="ManageBerkshelf">ManageBerkshelf</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#servicerolearn" title="ServiceRoleArn">ServiceRoleArn</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tags.md">Tags</a>, ... ]</i>,
        "<a href="#usecustomcookbooks" title="UseCustomCookbooks">UseCustomCookbooks</a>" : <i>Boolean</i>,
        "<a href="#useopsworkssecuritygroups" title="UseOpsworksSecurityGroups">UseOpsworksSecurityGroups</a>" : <i>Boolean</i>,
        "<a href="#vpcid" title="VpcId">VpcId</a>" : <i>String</i>,
        "<a href="#customcookbookssource" title="CustomCookbooksSource">CustomCookbooksSource</a>" : <i>[ <a href="customcookbookssource.md">CustomCookbooksSource</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::OpsworksStack
Properties:
    <a href="#agentversion" title="AgentVersion">AgentVersion</a>: <i>String</i>
    <a href="#berkshelfversion" title="BerkshelfVersion">BerkshelfVersion</a>: <i>String</i>
    <a href="#color" title="Color">Color</a>: <i>String</i>
    <a href="#configurationmanagername" title="ConfigurationManagerName">ConfigurationManagerName</a>: <i>String</i>
    <a href="#configurationmanagerversion" title="ConfigurationManagerVersion">ConfigurationManagerVersion</a>: <i>String</i>
    <a href="#customjson" title="CustomJson">CustomJson</a>: <i>String</i>
    <a href="#defaultavailabilityzone" title="DefaultAvailabilityZone">DefaultAvailabilityZone</a>: <i>String</i>
    <a href="#defaultinstanceprofilearn" title="DefaultInstanceProfileArn">DefaultInstanceProfileArn</a>: <i>String</i>
    <a href="#defaultos" title="DefaultOs">DefaultOs</a>: <i>String</i>
    <a href="#defaultrootdevicetype" title="DefaultRootDeviceType">DefaultRootDeviceType</a>: <i>String</i>
    <a href="#defaultsshkeyname" title="DefaultSshKeyName">DefaultSshKeyName</a>: <i>String</i>
    <a href="#defaultsubnetid" title="DefaultSubnetId">DefaultSubnetId</a>: <i>String</i>
    <a href="#hostnametheme" title="HostnameTheme">HostnameTheme</a>: <i>String</i>
    <a href="#manageberkshelf" title="ManageBerkshelf">ManageBerkshelf</a>: <i>Boolean</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#servicerolearn" title="ServiceRoleArn">ServiceRoleArn</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tags.md">Tags</a></i>
    <a href="#usecustomcookbooks" title="UseCustomCookbooks">UseCustomCookbooks</a>: <i>Boolean</i>
    <a href="#useopsworkssecuritygroups" title="UseOpsworksSecurityGroups">UseOpsworksSecurityGroups</a>: <i>Boolean</i>
    <a href="#vpcid" title="VpcId">VpcId</a>: <i>String</i>
    <a href="#customcookbookssource" title="CustomCookbooksSource">CustomCookbooksSource</a>: <i>
      - <a href="customcookbookssource.md">CustomCookbooksSource</a></i>
</pre>

## Properties

#### AgentVersion

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BerkshelfVersion

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Color

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConfigurationManagerName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConfigurationManagerVersion

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomJson

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultAvailabilityZone

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultInstanceProfileArn

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultOs

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultRootDeviceType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultSshKeyName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultSubnetId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HostnameTheme

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ManageBerkshelf

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceRoleArn

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of <a href="tags.md">Tags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseCustomCookbooks

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseOpsworksSecurityGroups

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomCookbooksSource

_Required_: No

_Type_: List of <a href="customcookbookssource.md">CustomCookbooksSource</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Arn

Returns the <code>Arn</code> value.

#### Id

Returns the <code>Id</code> value.

#### StackEndpoint

Returns the <code>StackEndpoint</code> value.

