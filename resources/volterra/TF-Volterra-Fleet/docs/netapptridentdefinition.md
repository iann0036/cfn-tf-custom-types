# TF::Volterra::Fleet NetappTridentDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#netappbackendontapnas" title="NetappBackendOntapNas">NetappBackendOntapNas</a>" : <i>[ <a href="netappbackendontapnasdefinition.md">NetappBackendOntapNasDefinition</a>, ... ]</i>,
    "<a href="#netappbackendontapsan" title="NetappBackendOntapSan">NetappBackendOntapSan</a>" : <i>[ <a href="netappbackendontapsandefinition.md">NetappBackendOntapSanDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#netappbackendontapnas" title="NetappBackendOntapNas">NetappBackendOntapNas</a>: <i>
      - <a href="netappbackendontapnasdefinition.md">NetappBackendOntapNasDefinition</a></i>
<a href="#netappbackendontapsan" title="NetappBackendOntapSan">NetappBackendOntapSan</a>: <i>
      - <a href="netappbackendontapsandefinition.md">NetappBackendOntapSanDefinition</a></i>
</pre>

## Properties

#### NetappBackendOntapNas

_Required_: No

_Type_: List of <a href="netappbackendontapnasdefinition.md">NetappBackendOntapNasDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetappBackendOntapSan

_Required_: No

_Type_: List of <a href="netappbackendontapsandefinition.md">NetappBackendOntapSanDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

