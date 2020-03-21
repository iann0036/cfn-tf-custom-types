# Terraform::AzureRM::BatchPool AutoUser

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#elevationlevel" title="ElevationLevel">ElevationLevel</a>" : <i>String</i>,
    "<a href="#scope" title="Scope">Scope</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#elevationlevel" title="ElevationLevel">ElevationLevel</a>: <i>String</i>
<a href="#scope" title="Scope">Scope</a>: <i>String</i>
</pre>

## Properties

#### ElevationLevel

The elevation level of the user identity under which the start task runs. Possible values are `Admin` or `NonAdmin`. Defaults to `NonAdmin`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Scope

The scope of the user identity under which the start task runs. Possible values are `Task` or `Pool`. Defaults to `Task`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

