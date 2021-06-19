# TF::Aviatrix::AwsTgw SecurityDomainsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#aviatrixfirewall" title="AviatrixFirewall">AviatrixFirewall</a>" : <i>Boolean</i>,
    "<a href="#connecteddomains" title="ConnectedDomains">ConnectedDomains</a>" : <i>[ String, ... ]</i>,
    "<a href="#nativeegress" title="NativeEgress">NativeEgress</a>" : <i>Boolean</i>,
    "<a href="#nativefirewall" title="NativeFirewall">NativeFirewall</a>" : <i>Boolean</i>,
    "<a href="#securitydomainname" title="SecurityDomainName">SecurityDomainName</a>" : <i>String</i>,
    "<a href="#attachedvpc" title="AttachedVpc">AttachedVpc</a>" : <i>[ <a href="attachedvpcdefinition.md">AttachedVpcDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#aviatrixfirewall" title="AviatrixFirewall">AviatrixFirewall</a>: <i>Boolean</i>
<a href="#connecteddomains" title="ConnectedDomains">ConnectedDomains</a>: <i>
      - String</i>
<a href="#nativeegress" title="NativeEgress">NativeEgress</a>: <i>Boolean</i>
<a href="#nativefirewall" title="NativeFirewall">NativeFirewall</a>: <i>Boolean</i>
<a href="#securitydomainname" title="SecurityDomainName">SecurityDomainName</a>: <i>String</i>
<a href="#attachedvpc" title="AttachedVpc">AttachedVpc</a>: <i>
      - <a href="attachedvpcdefinition.md">AttachedVpcDefinition</a></i>
</pre>

## Properties

#### AviatrixFirewall

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConnectedDomains

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NativeEgress

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NativeFirewall

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityDomainName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AttachedVpc

_Required_: No

_Type_: List of <a href="attachedvpcdefinition.md">AttachedVpcDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

