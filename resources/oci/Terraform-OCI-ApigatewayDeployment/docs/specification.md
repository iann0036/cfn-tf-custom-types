# Terraform::OCI::ApigatewayDeployment Specification

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#loggingpolicies" title="LoggingPolicies">LoggingPolicies</a>" : <i>[ &lt;a href=&#34;specification-loggingpolicies.md&#34;&gt;LoggingPolicies&lt;/a&gt;, ... ]</i>,
    "<a href="#requestpolicies" title="RequestPolicies">RequestPolicies</a>" : <i>[ &lt;a href=&#34;specification-requestpolicies.md&#34;&gt;RequestPolicies&lt;/a&gt;, ... ]</i>,
    "<a href="#routes" title="Routes">Routes</a>" : <i>[ &lt;a href=&#34;specification-routes.md&#34;&gt;Routes&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#loggingpolicies" title="LoggingPolicies">LoggingPolicies</a>: <i>
      - &lt;a href=&#34;specification-loggingpolicies.md&#34;&gt;LoggingPolicies&lt;/a&gt;</i>
<a href="#requestpolicies" title="RequestPolicies">RequestPolicies</a>: <i>
      - &lt;a href=&#34;specification-requestpolicies.md&#34;&gt;RequestPolicies&lt;/a&gt;</i>
<a href="#routes" title="Routes">Routes</a>: <i>
      - &lt;a href=&#34;specification-routes.md&#34;&gt;Routes&lt;/a&gt;</i>
</pre>

## Properties

#### LoggingPolicies

_Required_: No
_Type_: List of &lt;a href=&#34;specification-loggingpolicies.md&#34;&gt;LoggingPolicies&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestPolicies

_Required_: No
_Type_: List of &lt;a href=&#34;specification-requestpolicies.md&#34;&gt;RequestPolicies&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Routes

_Required_: No
_Type_: List of &lt;a href=&#34;specification-routes.md&#34;&gt;Routes&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

