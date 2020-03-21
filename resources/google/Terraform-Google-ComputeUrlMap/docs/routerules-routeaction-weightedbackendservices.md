# Terraform::Google::ComputeUrlMap RouteRules RouteAction WeightedBackendServices

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#backendservice" title="BackendService">BackendService</a>" : <i>String</i>,
    "<a href="#weight" title="Weight">Weight</a>" : <i>Double</i>,
    "<a href="#headeraction" title="HeaderAction">HeaderAction</a>" : <i>[ <a href="routerules-routeaction-weightedbackendservices-headeraction.md">HeaderAction</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#backendservice" title="BackendService">BackendService</a>: <i>String</i>
<a href="#weight" title="Weight">Weight</a>: <i>Double</i>
<a href="#headeraction" title="HeaderAction">HeaderAction</a>: <i>
      - <a href="routerules-routeaction-weightedbackendservices-headeraction.md">HeaderAction</a></i>
</pre>

## Properties

#### BackendService

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Weight

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HeaderAction

_Required_: No

_Type_: List of <a href="routerules-routeaction-weightedbackendservices-headeraction.md">HeaderAction</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

