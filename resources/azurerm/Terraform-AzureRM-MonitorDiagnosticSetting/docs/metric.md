# Terraform::AzureRM::MonitorDiagnosticSetting Metric

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#category" title="Category">Category</a>" : <i>String</i>,
    "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
    "<a href="#retentionpolicy" title="RetentionPolicy">RetentionPolicy</a>" : <i>[ <a href="metric-retentionpolicy.md">RetentionPolicy</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#category" title="Category">Category</a>: <i>String</i>
<a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
<a href="#retentionpolicy" title="RetentionPolicy">RetentionPolicy</a>: <i>
      - <a href="metric-retentionpolicy.md">RetentionPolicy</a></i>
</pre>

## Properties

#### Category

The name of a Diagnostic Metric Category for this Resource.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Enabled

Is this Diagnostic Metric enabled? Defaults to `true`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RetentionPolicy

_Required_: No

_Type_: List of <a href="metric-retentionpolicy.md">RetentionPolicy</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

