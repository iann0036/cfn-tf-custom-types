# TF::TencentCloud::ScfFunction

Provide a resource to create a SCF function.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::TencentCloud::ScfFunction",
    "Properties" : {
        "<a href="#clslogsetid" title="ClsLogsetId">ClsLogsetId</a>" : <i>String</i>,
        "<a href="#clstopicid" title="ClsTopicId">ClsTopicId</a>" : <i>String</i>,
        "<a href="#cosbucketname" title="CosBucketName">CosBucketName</a>" : <i>String</i>,
        "<a href="#cosbucketregion" title="CosBucketRegion">CosBucketRegion</a>" : <i>String</i>,
        "<a href="#cosobjectname" title="CosObjectName">CosObjectName</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#environment" title="Environment">Environment</a>" : <i>[ <a href="environmentdefinition.md">EnvironmentDefinition</a>, ... ]</i>,
        "<a href="#handler" title="Handler">Handler</a>" : <i>String</i>,
        "<a href="#l5enable" title="L5Enable">L5Enable</a>" : <i>Boolean</i>,
        "<a href="#memsize" title="MemSize">MemSize</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#namespace" title="Namespace">Namespace</a>" : <i>String</i>,
        "<a href="#role" title="Role">Role</a>" : <i>String</i>,
        "<a href="#runtime" title="Runtime">Runtime</a>" : <i>String</i>,
        "<a href="#subnetid" title="SubnetId">SubnetId</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#timeout" title="Timeout">Timeout</a>" : <i>Double</i>,
        "<a href="#vpcid" title="VpcId">VpcId</a>" : <i>String</i>,
        "<a href="#zipfile" title="ZipFile">ZipFile</a>" : <i>String</i>,
        "<a href="#triggers" title="Triggers">Triggers</a>" : <i>[ <a href="triggersdefinition.md">TriggersDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::TencentCloud::ScfFunction
Properties:
    <a href="#clslogsetid" title="ClsLogsetId">ClsLogsetId</a>: <i>String</i>
    <a href="#clstopicid" title="ClsTopicId">ClsTopicId</a>: <i>String</i>
    <a href="#cosbucketname" title="CosBucketName">CosBucketName</a>: <i>String</i>
    <a href="#cosbucketregion" title="CosBucketRegion">CosBucketRegion</a>: <i>String</i>
    <a href="#cosobjectname" title="CosObjectName">CosObjectName</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#environment" title="Environment">Environment</a>: <i>
      - <a href="environmentdefinition.md">EnvironmentDefinition</a></i>
    <a href="#handler" title="Handler">Handler</a>: <i>String</i>
    <a href="#l5enable" title="L5Enable">L5Enable</a>: <i>Boolean</i>
    <a href="#memsize" title="MemSize">MemSize</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#namespace" title="Namespace">Namespace</a>: <i>String</i>
    <a href="#role" title="Role">Role</a>: <i>String</i>
    <a href="#runtime" title="Runtime">Runtime</a>: <i>String</i>
    <a href="#subnetid" title="SubnetId">SubnetId</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#timeout" title="Timeout">Timeout</a>: <i>Double</i>
    <a href="#vpcid" title="VpcId">VpcId</a>: <i>String</i>
    <a href="#zipfile" title="ZipFile">ZipFile</a>: <i>String</i>
    <a href="#triggers" title="Triggers">Triggers</a>: <i>
      - <a href="triggersdefinition.md">TriggersDefinition</a></i>
</pre>

## Properties

#### ClsLogsetId

cls logset id of the SCF function.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClsTopicId

cls topic id of the SCF function.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CosBucketName

Cos bucket name of the SCF function, such as `cos-1234567890`, conflict with `zip_file`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CosBucketRegion

Cos bucket region of the SCF function, conflict with `zip_file`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CosObjectName

Cos object name of the SCF function, should have suffix `.zip` or `.jar`, conflict with `zip_file`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

Description of the SCF function. Description supports English letters, numbers, spaces, commas, newlines, periods and Chinese, the maximum length is 1000.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Environment

Environment of the SCF function.

_Required_: No

_Type_: List of <a href="environmentdefinition.md">EnvironmentDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Handler

Handler of the SCF function. The format of name is `<filename>.<method_name>`, and it supports 26 English letters, numbers, connectors, and underscores, it should start with a letter. The last character cannot be `-` or `_`. Available length is 2-60.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### L5Enable

Enable L5 for SCF function, default is `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MemSize

Memory size of the SCF function, unit is MB. The default is `128`MB. The range is 128M-1536M, and the ladder is 128M.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name of the SCF function. Name supports 26 English letters, numbers, connectors, and underscores, it should start with a letter. The last character cannot be `-` or `_`. Available length is 2-60.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Namespace

Namespace of the SCF function, default is `default`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Role

Role of the SCF function.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Runtime

Runtime of the SCF function, only supports `Python2.7`, `Python3.6`, `Nodejs6.10`, `Nodejs8.9`, `Nodejs10.15`, `PHP5`, `PHP7`, `Golang1`, and `Java8`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubnetId

Subnet ID of the SCF function.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

Tags of the SCF function.

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeout

Timeout of the SCF function, unit is second. Default `3`. Available value is 1-900.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcId

VPC ID of the SCF function.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ZipFile

Zip file of the SCF function, conflict with `cos_bucket_name`, `cos_object_name`, `cos_bucket_region`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Triggers

_Required_: No

_Type_: List of <a href="triggersdefinition.md">TriggersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### CodeError

Returns the <code>CodeError</code> value.

#### CodeResult

Returns the <code>CodeResult</code> value.

#### CodeSize

Returns the <code>CodeSize</code> value.

#### EipFixed

Returns the <code>EipFixed</code> value.

#### Eips

Returns the <code>Eips</code> value.

#### ErrNo

Returns the <code>ErrNo</code> value.

#### Host

Returns the <code>Host</code> value.

#### Id

Returns the <code>Id</code> value.

#### InstallDependency

Returns the <code>InstallDependency</code> value.

#### ModifyTime

Returns the <code>ModifyTime</code> value.

#### Status

Returns the <code>Status</code> value.

#### StatusDesc

Returns the <code>StatusDesc</code> value.

#### TriggerInfo

Returns the <code>TriggerInfo</code> value.

#### Vip

Returns the <code>Vip</code> value.

