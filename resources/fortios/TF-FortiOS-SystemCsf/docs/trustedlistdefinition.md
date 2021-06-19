# TF::FortiOS::SystemCsf TrustedListDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#action" title="Action">Action</a>" : <i>String</i>,
    "<a href="#authorizationtype" title="AuthorizationType">AuthorizationType</a>" : <i>String</i>,
    "<a href="#certificate" title="Certificate">Certificate</a>" : <i>String</i>,
    "<a href="#downstreamauthorization" title="DownstreamAuthorization">DownstreamAuthorization</a>" : <i>String</i>,
    "<a href="#hamembers" title="HaMembers">HaMembers</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#serial" title="Serial">Serial</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#action" title="Action">Action</a>: <i>String</i>
<a href="#authorizationtype" title="AuthorizationType">AuthorizationType</a>: <i>String</i>
<a href="#certificate" title="Certificate">Certificate</a>: <i>String</i>
<a href="#downstreamauthorization" title="DownstreamAuthorization">DownstreamAuthorization</a>: <i>String</i>
<a href="#hamembers" title="HaMembers">HaMembers</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#serial" title="Serial">Serial</a>: <i>String</i>
</pre>

## Properties

#### Action

Security fabric authorization action. Valid values: `accept`, `deny`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthorizationType

Authorization type. Valid values: `serial`, `certificate`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Certificate

Certificate.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DownstreamAuthorization

Trust authorizations by this node's administrator. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HaMembers

HA members.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Serial

Serial.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

