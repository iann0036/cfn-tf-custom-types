# Terraform::TencentCloud::ScfFunction

CloudFormation equivalent of tencentcloud_scf_function

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::TencentCloud::ScfFunction",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#clslogsetid" title="ClsLogsetId">ClsLogsetId</a>" : <i>String</i>,
        "<a href="#clstopicid" title="ClsTopicId">ClsTopicId</a>" : <i>String</i>,
        "<a href="#codeerror" title="CodeError">CodeError</a>" : <i>String</i>,
        "<a href="#coderesult" title="CodeResult">CodeResult</a>" : <i>String</i>,
        "<a href="#codesize" title="CodeSize">CodeSize</a>" : <i>Double</i>,
        "<a href="#cosbucketname" title="CosBucketName">CosBucketName</a>" : <i>String</i>,
        "<a href="#cosbucketregion" title="CosBucketRegion">CosBucketRegion</a>" : <i>String</i>,
        "<a href="#cosobjectname" title="CosObjectName">CosObjectName</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#eipfixed" title="EipFixed">EipFixed</a>" : <i>Boolean</i>,
        "<a href="#eips" title="Eips">Eips</a>" : <i>[ String, ... ]</i>,
        "<a href="#environment" title="Environment">Environment</a>" : <i>[ &lt;a href=&#34;environment.md&#34;&gt;Environment&lt;/a&gt;, ... ]</i>,
        "<a href="#errno" title="ErrNo">ErrNo</a>" : <i>Double</i>,
        "<a href="#handler" title="Handler">Handler</a>" : <i>String</i>,
        "<a href="#host" title="Host">Host</a>" : <i>String</i>,
        "<a href="#installdependency" title="InstallDependency">InstallDependency</a>" : <i>Boolean</i>,
        "<a href="#l5enable" title="L5Enable">L5Enable</a>" : <i>Boolean</i>,
        "<a href="#memsize" title="MemSize">MemSize</a>" : <i>Double</i>,
        "<a href="#modifytime" title="ModifyTime">ModifyTime</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#namespace" title="Namespace">Namespace</a>" : <i>String</i>,
        "<a href="#role" title="Role">Role</a>" : <i>String</i>,
        "<a href="#runtime" title="Runtime">Runtime</a>" : <i>String</i>,
        "<a href="#status" title="Status">Status</a>" : <i>String</i>,
        "<a href="#statusdesc" title="StatusDesc">StatusDesc</a>" : <i>String</i>,
        "<a href="#subnetid" title="SubnetId">SubnetId</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;, ... ]</i>,
        "<a href="#timeout" title="Timeout">Timeout</a>" : <i>Double</i>,
        "<a href="#triggerinfo" title="TriggerInfo">TriggerInfo</a>" : <i>[ &lt;a href=&#34;triggerinfo.md&#34;&gt;TriggerInfo&lt;/a&gt;, ... ]</i>,
        "<a href="#vip" title="Vip">Vip</a>" : <i>String</i>,
        "<a href="#vpcid" title="VpcId">VpcId</a>" : <i>String</i>,
        "<a href="#zipfile" title="ZipFile">ZipFile</a>" : <i>String</i>,
        "<a href="#triggers" title="Triggers">Triggers</a>" : <i>[ &lt;a href=&#34;triggers.md&#34;&gt;Triggers&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::TencentCloud::ScfFunction
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#clslogsetid" title="ClsLogsetId">ClsLogsetId</a>: <i>String</i>
    <a href="#clstopicid" title="ClsTopicId">ClsTopicId</a>: <i>String</i>
    <a href="#codeerror" title="CodeError">CodeError</a>: <i>String</i>
    <a href="#coderesult" title="CodeResult">CodeResult</a>: <i>String</i>
    <a href="#codesize" title="CodeSize">CodeSize</a>: <i>Double</i>
    <a href="#cosbucketname" title="CosBucketName">CosBucketName</a>: <i>String</i>
    <a href="#cosbucketregion" title="CosBucketRegion">CosBucketRegion</a>: <i>String</i>
    <a href="#cosobjectname" title="CosObjectName">CosObjectName</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#eipfixed" title="EipFixed">EipFixed</a>: <i>Boolean</i>
    <a href="#eips" title="Eips">Eips</a>: <i>
      - String</i>
    <a href="#environment" title="Environment">Environment</a>: <i>
      - &lt;a href=&#34;environment.md&#34;&gt;Environment&lt;/a&gt;</i>
    <a href="#errno" title="ErrNo">ErrNo</a>: <i>Double</i>
    <a href="#handler" title="Handler">Handler</a>: <i>String</i>
    <a href="#host" title="Host">Host</a>: <i>String</i>
    <a href="#installdependency" title="InstallDependency">InstallDependency</a>: <i>Boolean</i>
    <a href="#l5enable" title="L5Enable">L5Enable</a>: <i>Boolean</i>
    <a href="#memsize" title="MemSize">MemSize</a>: <i>Double</i>
    <a href="#modifytime" title="ModifyTime">ModifyTime</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#namespace" title="Namespace">Namespace</a>: <i>String</i>
    <a href="#role" title="Role">Role</a>: <i>String</i>
    <a href="#runtime" title="Runtime">Runtime</a>: <i>String</i>
    <a href="#status" title="Status">Status</a>: <i>String</i>
    <a href="#statusdesc" title="StatusDesc">StatusDesc</a>: <i>String</i>
    <a href="#subnetid" title="SubnetId">SubnetId</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;</i>
    <a href="#timeout" title="Timeout">Timeout</a>: <i>Double</i>
    <a href="#triggerinfo" title="TriggerInfo">TriggerInfo</a>: <i>
      - &lt;a href=&#34;triggerinfo.md&#34;&gt;TriggerInfo&lt;/a&gt;</i>
    <a href="#vip" title="Vip">Vip</a>: <i>String</i>
    <a href="#vpcid" title="VpcId">VpcId</a>: <i>String</i>
    <a href="#zipfile" title="ZipFile">ZipFile</a>: <i>String</i>
    <a href="#triggers" title="Triggers">Triggers</a>: <i>
      - &lt;a href=&#34;triggers.md&#34;&gt;Triggers&lt;/a&gt;</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClsLogsetId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClsTopicId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CodeError

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CodeResult

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CodeSize

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CosBucketName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CosBucketRegion

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CosObjectName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EipFixed

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Eips

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Environment

_Required_: No

_Type_: List of &lt;a href=&#34;environment.md&#34;&gt;Environment&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ErrNo

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Handler

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Host

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstallDependency

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### L5Enable

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MemSize

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ModifyTime

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Namespace

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Role

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Runtime

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StatusDesc

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubnetId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeout

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TriggerInfo

_Required_: No

_Type_: List of &lt;a href=&#34;triggerinfo.md&#34;&gt;TriggerInfo&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vip

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ZipFile

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Triggers

_Required_: No

_Type_: List of &lt;a href=&#34;triggers.md&#34;&gt;Triggers&lt;/a&gt;

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

Returns the &lt;code&gt;CodeError&lt;/code&gt; value.

#### CodeResult

Returns the &lt;code&gt;CodeResult&lt;/code&gt; value.

#### CodeSize

Returns the &lt;code&gt;CodeSize&lt;/code&gt; value.

#### EipFixed

Returns the &lt;code&gt;EipFixed&lt;/code&gt; value.

#### Eips

Returns the &lt;code&gt;Eips&lt;/code&gt; value.

#### ErrNo

Returns the &lt;code&gt;ErrNo&lt;/code&gt; value.

#### Host

Returns the &lt;code&gt;Host&lt;/code&gt; value.

#### InstallDependency

Returns the &lt;code&gt;InstallDependency&lt;/code&gt; value.

#### ModifyTime

Returns the &lt;code&gt;ModifyTime&lt;/code&gt; value.

#### Status

Returns the &lt;code&gt;Status&lt;/code&gt; value.

#### StatusDesc

Returns the &lt;code&gt;StatusDesc&lt;/code&gt; value.

#### TriggerInfo

Returns the &lt;code&gt;TriggerInfo&lt;/code&gt; value.

#### Vip

Returns the &lt;code&gt;Vip&lt;/code&gt; value.

