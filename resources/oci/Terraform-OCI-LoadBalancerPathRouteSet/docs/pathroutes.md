# Terraform::OCI::LoadBalancerPathRouteSet PathRoutes

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#backendsetname" title="BackendSetName">BackendSetName</a>" : <i>String</i>,
    "<a href="#path" title="Path">Path</a>" : <i>String</i>,
    "<a href="#pathmatchtype" title="PathMatchType">PathMatchType</a>" : <i>[ &lt;a href=&#34;pathroutes-pathmatchtype.md&#34;&gt;PathMatchType&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#backendsetname" title="BackendSetName">BackendSetName</a>: <i>String</i>
<a href="#path" title="Path">Path</a>: <i>String</i>
<a href="#pathmatchtype" title="PathMatchType">PathMatchType</a>: <i>
      - &lt;a href=&#34;pathroutes-pathmatchtype.md&#34;&gt;PathMatchType&lt;/a&gt;</i>
</pre>

## Properties

#### BackendSetName

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Path

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PathMatchType

_Required_: No
_Type_: List of &lt;a href=&#34;pathroutes-pathmatchtype.md&#34;&gt;PathMatchType&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

