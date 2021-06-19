# TF::AzureRM::MediaStreamingEndpoint AccessControlDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#akamaisignatureheaderauthenticationkey" title="AkamaiSignatureHeaderAuthenticationKey">AkamaiSignatureHeaderAuthenticationKey</a>" : <i>[ <a href="akamaisignatureheaderauthenticationkeydefinition.md">AkamaiSignatureHeaderAuthenticationKeyDefinition</a>, ... ]</i>,
    "<a href="#ipallow" title="IpAllow">IpAllow</a>" : <i>[ <a href="ipallowdefinition.md">IpAllowDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#akamaisignatureheaderauthenticationkey" title="AkamaiSignatureHeaderAuthenticationKey">AkamaiSignatureHeaderAuthenticationKey</a>: <i>
      - <a href="akamaisignatureheaderauthenticationkeydefinition.md">AkamaiSignatureHeaderAuthenticationKeyDefinition</a></i>
<a href="#ipallow" title="IpAllow">IpAllow</a>: <i>
      - <a href="ipallowdefinition.md">IpAllowDefinition</a></i>
</pre>

## Properties

#### AkamaiSignatureHeaderAuthenticationKey

_Required_: No

_Type_: List of <a href="akamaisignatureheaderauthenticationkeydefinition.md">AkamaiSignatureHeaderAuthenticationKeyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpAllow

_Required_: No

_Type_: List of <a href="ipallowdefinition.md">IpAllowDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

