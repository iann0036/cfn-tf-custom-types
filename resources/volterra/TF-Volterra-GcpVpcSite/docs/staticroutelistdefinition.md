# TF::Volterra::GcpVpcSite StaticRouteListDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#simplestaticroute" title="SimpleStaticRoute">SimpleStaticRoute</a>" : <i>String</i>,
    "<a href="#customstaticroute" title="CustomStaticRoute">CustomStaticRoute</a>" : <i>[ <a href="customstaticroutedefinition.md">CustomStaticRouteDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#simplestaticroute" title="SimpleStaticRoute">SimpleStaticRoute</a>: <i>String</i>
<a href="#customstaticroute" title="CustomStaticRoute">CustomStaticRoute</a>: <i>
      - <a href="customstaticroutedefinition.md">CustomStaticRouteDefinition</a></i>
</pre>

## Properties

#### SimpleStaticRoute

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomStaticRoute

_Required_: No

_Type_: List of <a href="customstaticroutedefinition.md">CustomStaticRouteDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

