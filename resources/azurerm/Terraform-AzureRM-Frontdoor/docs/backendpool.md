# Terraform::AzureRM::Frontdoor BackendPool

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#healthprobename" title="HealthProbeName">HealthProbeName</a>" : <i>String</i>,
    "<a href="#loadbalancingname" title="LoadBalancingName">LoadBalancingName</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#backend" title="Backend">Backend</a>" : <i>[ &lt;a href=&#34;backendpool-backend.md&#34;&gt;Backend&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#healthprobename" title="HealthProbeName">HealthProbeName</a>: <i>String</i>
<a href="#loadbalancingname" title="LoadBalancingName">LoadBalancingName</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#backend" title="Backend">Backend</a>: <i>
      - &lt;a href=&#34;backendpool-backend.md&#34;&gt;Backend&lt;/a&gt;</i>
</pre>

## Properties

#### HealthProbeName

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoadBalancingName

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Backend

_Required_: No
_Type_: List of &lt;a href=&#34;backendpool-backend.md&#34;&gt;Backend&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

