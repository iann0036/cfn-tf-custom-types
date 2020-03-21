# Terraform::NS1::Record Filters

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#config" title="Config">Config</a>" : <i>[ <a href="filters-config.md">Config</a>, ... ]</i>,
    "<a href="#disabled" title="Disabled">Disabled</a>" : <i>Boolean</i>,
    "<a href="#filter" title="Filter">Filter</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#config" title="Config">Config</a>: <i>
      - <a href="filters-config.md">Config</a></i>
<a href="#disabled" title="Disabled">Disabled</a>: <i>Boolean</i>
<a href="#filter" title="Filter">Filter</a>: <i>String</i>
</pre>

## Properties

#### Config

_Required_: No

_Type_: List of <a href="filters-config.md">Config</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Disabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Filter

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

