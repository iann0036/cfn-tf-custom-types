# TF::FortiOS::IcapProfile RespmodForwardRulesDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#action" title="Action">Action</a>" : <i>String</i>,
    "<a href="#host" title="Host">Host</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#headergroup" title="HeaderGroup">HeaderGroup</a>" : <i>[ <a href="headergroupdefinition.md">HeaderGroupDefinition</a>, ... ]</i>,
    "<a href="#httprespstatuscode" title="HttpRespStatusCode">HttpRespStatusCode</a>" : <i>[ <a href="httprespstatuscodedefinition.md">HttpRespStatusCodeDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#action" title="Action">Action</a>: <i>String</i>
<a href="#host" title="Host">Host</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#headergroup" title="HeaderGroup">HeaderGroup</a>: <i>
      - <a href="headergroupdefinition.md">HeaderGroupDefinition</a></i>
<a href="#httprespstatuscode" title="HttpRespStatusCode">HttpRespStatusCode</a>: <i>
      - <a href="httprespstatuscodedefinition.md">HttpRespStatusCodeDefinition</a></i>
</pre>

## Properties

#### Action

Action to be taken for ICAP server. Valid values: `forward`, `bypass`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Host

Address object for the host.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Address name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HeaderGroup

_Required_: No

_Type_: List of <a href="headergroupdefinition.md">HeaderGroupDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpRespStatusCode

_Required_: No

_Type_: List of <a href="httprespstatuscodedefinition.md">HttpRespStatusCodeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

