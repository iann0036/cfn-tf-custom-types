# TF::GoogleBeta::GoogleSecurityScannerScanConfig AuthenticationDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#customaccount" title="CustomAccount">CustomAccount</a>" : <i>[ <a href="customaccountdefinition.md">CustomAccountDefinition</a>, ... ]</i>,
    "<a href="#googleaccount" title="GoogleAccount">GoogleAccount</a>" : <i>[ <a href="googleaccountdefinition.md">GoogleAccountDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#customaccount" title="CustomAccount">CustomAccount</a>: <i>
      - <a href="customaccountdefinition.md">CustomAccountDefinition</a></i>
<a href="#googleaccount" title="GoogleAccount">GoogleAccount</a>: <i>
      - <a href="googleaccountdefinition.md">GoogleAccountDefinition</a></i>
</pre>

## Properties

#### CustomAccount

_Required_: No

_Type_: List of <a href="customaccountdefinition.md">CustomAccountDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GoogleAccount

_Required_: No

_Type_: List of <a href="googleaccountdefinition.md">GoogleAccountDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

