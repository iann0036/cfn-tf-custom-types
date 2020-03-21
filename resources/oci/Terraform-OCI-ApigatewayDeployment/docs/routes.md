# Terraform::OCI::ApigatewayDeployment Routes

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#methods" title="Methods">Methods</a>" : <i>[ String, ... ]</i>,
    "<a href="#path" title="Path">Path</a>" : <i>String</i>,
    "<a href="#backend" title="Backend">Backend</a>" : <i>[ &lt;a href=&#34;routes-backend.md&#34;&gt;Backend&lt;/a&gt;, ... ]</i>,
    "<a href="#loggingpolicies" title="LoggingPolicies">LoggingPolicies</a>" : <i>[ &lt;a href=&#34;routes-loggingpolicies.md&#34;&gt;LoggingPolicies&lt;/a&gt;, ... ]</i>,
    "<a href="#requestpolicies" title="RequestPolicies">RequestPolicies</a>" : <i>[ &lt;a href=&#34;routes-requestpolicies.md&#34;&gt;RequestPolicies&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#methods" title="Methods">Methods</a>: <i>
      - String</i>
<a href="#path" title="Path">Path</a>: <i>String</i>
<a href="#backend" title="Backend">Backend</a>: <i>
      - &lt;a href=&#34;routes-backend.md&#34;&gt;Backend&lt;/a&gt;</i>
<a href="#loggingpolicies" title="LoggingPolicies">LoggingPolicies</a>: <i>
      - &lt;a href=&#34;routes-loggingpolicies.md&#34;&gt;LoggingPolicies&lt;/a&gt;</i>
<a href="#requestpolicies" title="RequestPolicies">RequestPolicies</a>: <i>
      - &lt;a href=&#34;routes-requestpolicies.md&#34;&gt;RequestPolicies&lt;/a&gt;</i>
</pre>

## Properties

#### Methods

_Required_: No
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Path

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Backend

_Required_: No
_Type_: List of &lt;a href=&#34;routes-backend.md&#34;&gt;Backend&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoggingPolicies

_Required_: No
_Type_: List of &lt;a href=&#34;routes-loggingpolicies.md&#34;&gt;LoggingPolicies&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestPolicies

_Required_: No
_Type_: List of &lt;a href=&#34;routes-requestpolicies.md&#34;&gt;RequestPolicies&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

