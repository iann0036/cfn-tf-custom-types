# Terraform::OCI::ApigatewayDeployment Authentication

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#functionid" title="FunctionId">FunctionId</a>" : <i>String</i>,
    "<a href="#isanonymousaccessallowed" title="IsAnonymousAccessAllowed">IsAnonymousAccessAllowed</a>" : <i>Boolean</i>,
    "<a href="#tokenheader" title="TokenHeader">TokenHeader</a>" : <i>String</i>,
    "<a href="#tokenqueryparam" title="TokenQueryParam">TokenQueryParam</a>" : <i>String</i>,
    "<a href="#type" title="Type">Type</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#functionid" title="FunctionId">FunctionId</a>: <i>String</i>
<a href="#isanonymousaccessallowed" title="IsAnonymousAccessAllowed">IsAnonymousAccessAllowed</a>: <i>Boolean</i>
<a href="#tokenheader" title="TokenHeader">TokenHeader</a>: <i>String</i>
<a href="#tokenqueryparam" title="TokenQueryParam">TokenQueryParam</a>: <i>String</i>
<a href="#type" title="Type">Type</a>: <i>String</i>
</pre>

## Properties

#### FunctionId

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsAnonymousAccessAllowed

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TokenHeader

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TokenQueryParam

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

