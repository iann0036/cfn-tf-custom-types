# TF::Datadog::SyntheticsTest BrowserStepDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#allowfailure" title="AllowFailure">AllowFailure</a>" : <i>Boolean</i>,
    "<a href="#forceelementupdate" title="ForceElementUpdate">ForceElementUpdate</a>" : <i>Boolean</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#timeout" title="Timeout">Timeout</a>" : <i>Double</i>,
    "<a href="#type" title="Type">Type</a>" : <i>String</i>,
    "<a href="#params" title="Params">Params</a>" : <i>[ <a href="paramsdefinition.md">ParamsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#allowfailure" title="AllowFailure">AllowFailure</a>: <i>Boolean</i>
<a href="#forceelementupdate" title="ForceElementUpdate">ForceElementUpdate</a>: <i>Boolean</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#timeout" title="Timeout">Timeout</a>: <i>Double</i>
<a href="#type" title="Type">Type</a>: <i>String</i>
<a href="#params" title="Params">Params</a>: <i>
      - <a href="paramsdefinition.md">ParamsDefinition</a></i>
</pre>

## Properties

#### AllowFailure

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForceElementUpdate

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeout

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Params

_Required_: No

_Type_: List of <a href="paramsdefinition.md">ParamsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

