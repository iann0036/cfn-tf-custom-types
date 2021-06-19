# TF::SumoLogic::Dashboard PanelDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#sumosearchpanel" title="SumoSearchPanel">SumoSearchPanel</a>" : <i>[ <a href="sumosearchpaneldefinition.md">SumoSearchPanelDefinition</a>, ... ]</i>,
    "<a href="#textpanel" title="TextPanel">TextPanel</a>" : <i>[ <a href="textpaneldefinition.md">TextPanelDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#sumosearchpanel" title="SumoSearchPanel">SumoSearchPanel</a>: <i>
      - <a href="sumosearchpaneldefinition.md">SumoSearchPanelDefinition</a></i>
<a href="#textpanel" title="TextPanel">TextPanel</a>: <i>
      - <a href="textpaneldefinition.md">TextPanelDefinition</a></i>
</pre>

## Properties

#### SumoSearchPanel

_Required_: No

_Type_: List of <a href="sumosearchpaneldefinition.md">SumoSearchPanelDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TextPanel

_Required_: No

_Type_: List of <a href="textpaneldefinition.md">TextPanelDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

