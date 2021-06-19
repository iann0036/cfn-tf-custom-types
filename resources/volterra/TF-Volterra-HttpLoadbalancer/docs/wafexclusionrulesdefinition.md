# TF::Volterra::HttpLoadbalancer WafExclusionRulesDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#anydomain" title="AnyDomain">AnyDomain</a>" : <i>Boolean</i>,
    "<a href="#domainregex" title="DomainRegex">DomainRegex</a>" : <i>String</i>,
    "<a href="#excluderuleids" title="ExcludeRuleIds">ExcludeRuleIds</a>" : <i>[ String, ... ]</i>,
    "<a href="#expirationtimestamp" title="ExpirationTimestamp">ExpirationTimestamp</a>" : <i>String</i>,
    "<a href="#methods" title="Methods">Methods</a>" : <i>[ String, ... ]</i>,
    "<a href="#pathregex" title="PathRegex">PathRegex</a>" : <i>String</i>,
    "<a href="#metadata" title="Metadata">Metadata</a>" : <i>[ <a href="metadatadefinition.md">MetadataDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#anydomain" title="AnyDomain">AnyDomain</a>: <i>Boolean</i>
<a href="#domainregex" title="DomainRegex">DomainRegex</a>: <i>String</i>
<a href="#excluderuleids" title="ExcludeRuleIds">ExcludeRuleIds</a>: <i>
      - String</i>
<a href="#expirationtimestamp" title="ExpirationTimestamp">ExpirationTimestamp</a>: <i>String</i>
<a href="#methods" title="Methods">Methods</a>: <i>
      - String</i>
<a href="#pathregex" title="PathRegex">PathRegex</a>: <i>String</i>
<a href="#metadata" title="Metadata">Metadata</a>: <i>
      - <a href="metadatadefinition.md">MetadataDefinition</a></i>
</pre>

## Properties

#### AnyDomain

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DomainRegex

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExcludeRuleIds

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExpirationTimestamp

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Methods

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PathRegex

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Metadata

_Required_: No

_Type_: List of <a href="metadatadefinition.md">MetadataDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

