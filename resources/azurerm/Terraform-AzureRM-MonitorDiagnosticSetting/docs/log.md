# Terraform::AzureRM::MonitorDiagnosticSetting Log

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#category" title="Category">Category</a>" : <i>String</i>,
    "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
    "<a href="#retentionpolicy" title="RetentionPolicy">RetentionPolicy</a>" : <i>[ &lt;a href=&#34;log-retentionpolicy.md&#34;&gt;RetentionPolicy&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#category" title="Category">Category</a>: <i>String</i>
<a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
<a href="#retentionpolicy" title="RetentionPolicy">RetentionPolicy</a>: <i>
      - &lt;a href=&#34;log-retentionpolicy.md&#34;&gt;RetentionPolicy&lt;/a&gt;</i>
</pre>

## Properties

#### Category

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Enabled

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RetentionPolicy

_Required_: No
_Type_: List of &lt;a href=&#34;log-retentionpolicy.md&#34;&gt;RetentionPolicy&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

