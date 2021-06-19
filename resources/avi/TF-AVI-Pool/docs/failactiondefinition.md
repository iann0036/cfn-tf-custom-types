# TF::AVI::Pool FailActionDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#type" title="Type">Type</a>" : <i>String</i>,
    "<a href="#localrsp" title="LocalRsp">LocalRsp</a>" : <i>[ <a href="localrspdefinition.md">LocalRspDefinition</a>, ... ]</i>,
    "<a href="#redirect" title="Redirect">Redirect</a>" : <i>[ <a href="redirectdefinition.md">RedirectDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#type" title="Type">Type</a>: <i>String</i>
<a href="#localrsp" title="LocalRsp">LocalRsp</a>: <i>
      - <a href="localrspdefinition.md">LocalRspDefinition</a></i>
<a href="#redirect" title="Redirect">Redirect</a>: <i>
      - <a href="redirectdefinition.md">RedirectDefinition</a></i>
</pre>

## Properties

#### Type

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocalRsp

_Required_: No

_Type_: List of <a href="localrspdefinition.md">LocalRspDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Redirect

_Required_: No

_Type_: List of <a href="redirectdefinition.md">RedirectDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

