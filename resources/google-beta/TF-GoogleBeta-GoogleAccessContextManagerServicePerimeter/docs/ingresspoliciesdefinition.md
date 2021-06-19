# TF::GoogleBeta::GoogleAccessContextManagerServicePerimeter IngressPoliciesDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#ingressfrom" title="IngressFrom">IngressFrom</a>" : <i>[ <a href="ingressfromdefinition.md">IngressFromDefinition</a>, ... ]</i>,
    "<a href="#ingressto" title="IngressTo">IngressTo</a>" : <i>[ <a href="ingresstodefinition.md">IngressToDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#ingressfrom" title="IngressFrom">IngressFrom</a>: <i>
      - <a href="ingressfromdefinition.md">IngressFromDefinition</a></i>
<a href="#ingressto" title="IngressTo">IngressTo</a>: <i>
      - <a href="ingresstodefinition.md">IngressToDefinition</a></i>
</pre>

## Properties

#### IngressFrom

_Required_: No

_Type_: List of <a href="ingressfromdefinition.md">IngressFromDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IngressTo

_Required_: No

_Type_: List of <a href="ingresstodefinition.md">IngressToDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

