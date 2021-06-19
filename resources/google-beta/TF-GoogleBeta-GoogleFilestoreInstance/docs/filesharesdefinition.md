# TF::GoogleBeta::GoogleFilestoreInstance FileSharesDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#capacitygb" title="CapacityGb">CapacityGb</a>" : <i>Double</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#nfsexportoptions" title="NfsExportOptions">NfsExportOptions</a>" : <i>[ <a href="nfsexportoptionsdefinition.md">NfsExportOptionsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#capacitygb" title="CapacityGb">CapacityGb</a>: <i>Double</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#nfsexportoptions" title="NfsExportOptions">NfsExportOptions</a>: <i>
      - <a href="nfsexportoptionsdefinition.md">NfsExportOptionsDefinition</a></i>
</pre>

## Properties

#### CapacityGb

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NfsExportOptions

_Required_: No

_Type_: List of <a href="nfsexportoptionsdefinition.md">NfsExportOptionsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

