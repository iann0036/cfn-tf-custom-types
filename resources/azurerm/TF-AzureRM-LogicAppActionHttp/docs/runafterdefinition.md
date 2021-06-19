# TF::AzureRM::LogicAppActionHttp RunAfterDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#actionname" title="ActionName">ActionName</a>" : <i>String</i>,
    "<a href="#actionresult" title="ActionResult">ActionResult</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#actionname" title="ActionName">ActionName</a>: <i>String</i>
<a href="#actionresult" title="ActionResult">ActionResult</a>: <i>String</i>
</pre>

## Properties

#### ActionName

Specifies the name of the precedent HTTP Action.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ActionResult

Specifies the expected result of the precedent HTTP Action, only after which the current HTTP Action will be triggered. Possible values include `Succeeded`, `Failed`, `Skipped` and `TimedOut`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

