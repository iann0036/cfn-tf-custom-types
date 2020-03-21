# Terraform::OCI::LoadBalancerPathRouteSet PathRoutes

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#backendsetname" title="BackendSetName">BackendSetName</a>" : <i>String</i>,
    "<a href="#path" title="Path">Path</a>" : <i>String</i>,
    "<a href="#pathmatchtype" title="PathMatchType">PathMatchType</a>" : <i>[ <a href="pathroutes-pathmatchtype.md">PathMatchType</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#backendsetname" title="BackendSetName">BackendSetName</a>: <i>String</i>
<a href="#path" title="Path">Path</a>: <i>String</i>
<a href="#pathmatchtype" title="PathMatchType">PathMatchType</a>: <i>
      - <a href="pathroutes-pathmatchtype.md">PathMatchType</a></i>
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

_Type_: List of <a href="pathroutes-pathmatchtype.md">PathMatchType</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

