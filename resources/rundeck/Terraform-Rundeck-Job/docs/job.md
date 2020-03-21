# Terraform::Rundeck::Job Job

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#args" title="Args">Args</a>" : <i>String</i>,
    "<a href="#groupname" title="GroupName">GroupName</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#nodefilters" title="Nodefilters">Nodefilters</a>" : <i>[ <a href="job-nodefilters.md">Nodefilters</a>, ... ]</i>,
    "<a href="#runforeachnode" title="RunForEachNode">RunForEachNode</a>" : <i>Boolean</i>
}
</pre>

### YAML

<pre>
<a href="#args" title="Args">Args</a>: <i>String</i>
<a href="#groupname" title="GroupName">GroupName</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#nodefilters" title="Nodefilters">Nodefilters</a>: <i>
      - <a href="job-nodefilters.md">Nodefilters</a></i>
<a href="#runforeachnode" title="RunForEachNode">RunForEachNode</a>: <i>Boolean</i>
</pre>

## Properties

#### Args

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GroupName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Nodefilters

_Required_: No

_Type_: List of <a href="job-nodefilters.md">Nodefilters</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RunForEachNode

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

