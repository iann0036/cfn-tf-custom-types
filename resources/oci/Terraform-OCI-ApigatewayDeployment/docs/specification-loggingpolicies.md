# Terraform::OCI::ApigatewayDeployment Specification LoggingPolicies

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#accesslog" title="AccessLog">AccessLog</a>" : <i>[ &lt;a href=&#34;specification-loggingpolicies-accesslog.md&#34;&gt;AccessLog&lt;/a&gt;, ... ]</i>,
    "<a href="#executionlog" title="ExecutionLog">ExecutionLog</a>" : <i>[ &lt;a href=&#34;specification-loggingpolicies-executionlog.md&#34;&gt;ExecutionLog&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#accesslog" title="AccessLog">AccessLog</a>: <i>
      - &lt;a href=&#34;specification-loggingpolicies-accesslog.md&#34;&gt;AccessLog&lt;/a&gt;</i>
<a href="#executionlog" title="ExecutionLog">ExecutionLog</a>: <i>
      - &lt;a href=&#34;specification-loggingpolicies-executionlog.md&#34;&gt;ExecutionLog&lt;/a&gt;</i>
</pre>

## Properties

#### AccessLog

_Required_: No
_Type_: List of &lt;a href=&#34;specification-loggingpolicies-accesslog.md&#34;&gt;AccessLog&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExecutionLog

_Required_: No
_Type_: List of &lt;a href=&#34;specification-loggingpolicies-executionlog.md&#34;&gt;ExecutionLog&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

