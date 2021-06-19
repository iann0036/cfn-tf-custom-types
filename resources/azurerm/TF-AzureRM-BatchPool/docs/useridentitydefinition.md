# TF::AzureRM::BatchPool UserIdentityDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#username" title="UserName">UserName</a>" : <i>String</i>,
    "<a href="#autouser" title="AutoUser">AutoUser</a>" : <i>[ <a href="autouserdefinition.md">AutoUserDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#username" title="UserName">UserName</a>: <i>String</i>
<a href="#autouser" title="AutoUser">AutoUser</a>: <i>
      - <a href="autouserdefinition.md">AutoUserDefinition</a></i>
</pre>

## Properties

#### UserName

The username to be used by the Batch pool start task.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoUser

_Required_: No

_Type_: List of <a href="autouserdefinition.md">AutoUserDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

