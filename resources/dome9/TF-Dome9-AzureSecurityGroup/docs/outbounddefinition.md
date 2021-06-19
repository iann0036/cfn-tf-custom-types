# TF::Dome9::AzureSecurityGroup OutboundDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#access" title="Access">Access</a>" : <i>String</i>,
    "<a href="#description" title="Description">Description</a>" : <i>String</i>,
    "<a href="#destinationportranges" title="DestinationPortRanges">DestinationPortRanges</a>" : <i>[ String, ... ]</i>,
    "<a href="#isdefault" title="IsDefault">IsDefault</a>" : <i>Boolean</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#priority" title="Priority">Priority</a>" : <i>Double</i>,
    "<a href="#protocol" title="Protocol">Protocol</a>" : <i>String</i>,
    "<a href="#sourceportranges" title="SourcePortRanges">SourcePortRanges</a>" : <i>[ String, ... ]</i>,
    "<a href="#destinationscopes" title="DestinationScopes">DestinationScopes</a>" : <i>[ <a href="destinationscopesdefinition.md">DestinationScopesDefinition</a>, ... ]</i>,
    "<a href="#sourcescopes" title="SourceScopes">SourceScopes</a>" : <i>[ <a href="sourcescopesdefinition.md">SourceScopesDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#access" title="Access">Access</a>: <i>String</i>
<a href="#description" title="Description">Description</a>: <i>String</i>
<a href="#destinationportranges" title="DestinationPortRanges">DestinationPortRanges</a>: <i>
      - String</i>
<a href="#isdefault" title="IsDefault">IsDefault</a>: <i>Boolean</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#priority" title="Priority">Priority</a>: <i>Double</i>
<a href="#protocol" title="Protocol">Protocol</a>: <i>String</i>
<a href="#sourceportranges" title="SourcePortRanges">SourcePortRanges</a>: <i>
      - String</i>
<a href="#destinationscopes" title="DestinationScopes">DestinationScopes</a>: <i>
      - <a href="destinationscopesdefinition.md">DestinationScopesDefinition</a></i>
<a href="#sourcescopes" title="SourceScopes">SourceScopes</a>: <i>
      - <a href="sourcescopesdefinition.md">SourceScopesDefinition</a></i>
</pre>

## Properties

#### Access

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DestinationPortRanges

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsDefault

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Priority

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Protocol

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourcePortRanges

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DestinationScopes

_Required_: No

_Type_: List of <a href="destinationscopesdefinition.md">DestinationScopesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceScopes

_Required_: No

_Type_: List of <a href="sourcescopesdefinition.md">SourceScopesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

