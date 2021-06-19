# TF::AWS::OpsworksStack

Provides an OpsWorks stack resource.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::OpsworksStack",
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
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#tagsall" title="TagsAll">TagsAll</a>" : <i>[ <a href="tagsalldefinition.md">TagsAllDefinition</a>, ... ]</i>,
        "<a href="#usecustomcookbooks" title="UseCustomCookbooks">UseCustomCookbooks</a>" : <i>Boolean</i>,
        "<a href="#useopsworkssecuritygroups" title="UseOpsworksSecurityGroups">UseOpsworksSecurityGroups</a>" : <i>Boolean</i>,
        "<a href="#vpcid" title="VpcId">VpcId</a>" : <i>String</i>,
        "<a href="#customcookbookssource" title="CustomCookbooksSource">CustomCookbooksSource</a>" : <i>[ <a href="customcookbookssourcedefinition.md">CustomCookbooksSourceDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::OpsworksStack
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
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#tagsall" title="TagsAll">TagsAll</a>: <i>
      - <a href="tagsalldefinition.md">TagsAllDefinition</a></i>
    <a href="#usecustomcookbooks" title="UseCustomCookbooks">UseCustomCookbooks</a>: <i>Boolean</i>
    <a href="#useopsworkssecuritygroups" title="UseOpsworksSecurityGroups">UseOpsworksSecurityGroups</a>: <i>Boolean</i>
    <a href="#vpcid" title="VpcId">VpcId</a>: <i>String</i>
    <a href="#customcookbookssource" title="CustomCookbooksSource">CustomCookbooksSource</a>: <i>
      - <a href="customcookbookssourcedefinition.md">CustomCookbooksSourceDefinition</a></i>
</pre>

## Properties

#### AgentVersion

If set to `"LATEST"`, OpsWorks will automatically install the latest version.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BerkshelfVersion

If `manage_berkshelf` is enabled, the version of Berkshelf to use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Color

Color to paint next to the stack's resources in the OpsWorks console.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConfigurationManagerName

Name of the configuration manager to use. Defaults to "Chef".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConfigurationManagerVersion

Version of the configuration manager to use. Defaults to "11.4".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomJson

Custom JSON attributes to apply to the entire stack.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultAvailabilityZone

Name of the availability zone where instances will be created
by default. This is required unless you set `vpc_id`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultInstanceProfileArn

The ARN of an IAM Instance Profile that created instances
will have by default.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultOs

Name of OS that will be installed on instances by default.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultRootDeviceType

Name of the type of root device instances will have by default.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultSshKeyName

Name of the SSH keypair that instances will have by default.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultSubnetId

Id of the subnet in which instances will be created by default. Mandatory
if `vpc_id` is set, and forbidden if it isn't.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HostnameTheme

Keyword representing the naming scheme that will be used for instance hostnames
within this stack.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ManageBerkshelf

Boolean value controlling whether Opsworks will run Berkshelf for this stack.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the stack.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

The name of the region where the stack will exist.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceRoleArn

The ARN of an IAM role that the OpsWorks service will act as.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A map of tags to assign to the resource. If configured with a provider [`default_tags` configuration block](/docs/providers/aws/index.html#default_tags-configuration-block) present, tags with matching keys will overwrite those defined at the provider-level.

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TagsAll

_Required_: No

_Type_: List of <a href="tagsalldefinition.md">TagsAllDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseCustomCookbooks

Boolean value controlling whether the custom cookbook settings are
enabled.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseOpsworksSecurityGroups

Boolean value controlling whether the standard OpsWorks
security groups apply to created instances.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcId

The id of the VPC that this stack belongs to.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomCookbooksSource

_Required_: No

_Type_: List of <a href="customcookbookssourcedefinition.md">CustomCookbooksSourceDefinition</a>

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

