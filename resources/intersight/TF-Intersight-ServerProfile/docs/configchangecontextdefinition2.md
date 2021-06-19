# TF::Intersight::ServerProfile ConfigChangeContextDefinition2

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#additionalproperties" title="AdditionalProperties">AdditionalProperties</a>" : <i>String</i>,
    "<a href="#classid" title="ClassId">ClassId</a>" : <i>String</i>,
    "<a href="#configchangeerror" title="ConfigChangeError">ConfigChangeError</a>" : <i>String</i>,
    "<a href="#configchangestate" title="ConfigChangeState">ConfigChangeState</a>" : <i>String</i>,
    "<a href="#initialconfigcontext" title="InitialConfigContext">InitialConfigContext</a>" : <i>[ <a href="configchangecontextdefinition.md">ConfigChangeContextDefinition</a>, ... ]</i>,
    "<a href="#objecttype" title="ObjectType">ObjectType</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#additionalproperties" title="AdditionalProperties">AdditionalProperties</a>: <i>String</i>
<a href="#classid" title="ClassId">ClassId</a>: <i>String</i>
<a href="#configchangeerror" title="ConfigChangeError">ConfigChangeError</a>: <i>String</i>
<a href="#configchangestate" title="ConfigChangeState">ConfigChangeState</a>: <i>String</i>
<a href="#initialconfigcontext" title="InitialConfigContext">InitialConfigContext</a>: <i>
      - <a href="configchangecontextdefinition.md">ConfigChangeContextDefinition</a></i>
<a href="#objecttype" title="ObjectType">ObjectType</a>: <i>String</i>
</pre>

## Properties

#### AdditionalProperties

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClassId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConfigChangeError

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConfigChangeState

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InitialConfigContext

_Required_: No

_Type_: List of <a href="configchangecontextdefinition.md">ConfigChangeContextDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ObjectType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

