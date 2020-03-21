# Terraform::AzureRM::AppServiceSlot Logs

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#applicationlogs" title="ApplicationLogs">ApplicationLogs</a>" : <i>[ &lt;a href=&#34;logs-applicationlogs.md&#34;&gt;ApplicationLogs&lt;/a&gt;, ... ]</i>,
    "<a href="#httplogs" title="HttpLogs">HttpLogs</a>" : <i>[ &lt;a href=&#34;logs-httplogs.md&#34;&gt;HttpLogs&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#applicationlogs" title="ApplicationLogs">ApplicationLogs</a>: <i>
      - &lt;a href=&#34;logs-applicationlogs.md&#34;&gt;ApplicationLogs&lt;/a&gt;</i>
<a href="#httplogs" title="HttpLogs">HttpLogs</a>: <i>
      - &lt;a href=&#34;logs-httplogs.md&#34;&gt;HttpLogs&lt;/a&gt;</i>
</pre>

## Properties

#### ApplicationLogs

_Required_: No
_Type_: List of &lt;a href=&#34;logs-applicationlogs.md&#34;&gt;ApplicationLogs&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpLogs

_Required_: No
_Type_: List of &lt;a href=&#34;logs-httplogs.md&#34;&gt;HttpLogs&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

