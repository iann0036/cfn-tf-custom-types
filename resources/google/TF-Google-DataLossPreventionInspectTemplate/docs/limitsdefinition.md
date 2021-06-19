# TF::Google::DataLossPreventionInspectTemplate LimitsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#maxfindingsperitem" title="MaxFindingsPerItem">MaxFindingsPerItem</a>" : <i>Double</i>,
    "<a href="#maxfindingsperrequest" title="MaxFindingsPerRequest">MaxFindingsPerRequest</a>" : <i>Double</i>,
    "<a href="#maxfindingsperinfotype" title="MaxFindingsPerInfoType">MaxFindingsPerInfoType</a>" : <i>[ <a href="maxfindingsperinfotypedefinition.md">MaxFindingsPerInfoTypeDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#maxfindingsperitem" title="MaxFindingsPerItem">MaxFindingsPerItem</a>: <i>Double</i>
<a href="#maxfindingsperrequest" title="MaxFindingsPerRequest">MaxFindingsPerRequest</a>: <i>Double</i>
<a href="#maxfindingsperinfotype" title="MaxFindingsPerInfoType">MaxFindingsPerInfoType</a>: <i>
      - <a href="maxfindingsperinfotypedefinition.md">MaxFindingsPerInfoTypeDefinition</a></i>
</pre>

## Properties

#### MaxFindingsPerItem

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxFindingsPerRequest

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxFindingsPerInfoType

_Required_: No

_Type_: List of <a href="maxfindingsperinfotypedefinition.md">MaxFindingsPerInfoTypeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

