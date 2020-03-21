# Terraform::AzureRM::VpnServerConfiguration RadiusServer

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#address" title="Address">Address</a>" : <i>String</i>,
    "<a href="#secret" title="Secret">Secret</a>" : <i>String</i>,
    "<a href="#clientrootcertificate" title="ClientRootCertificate">ClientRootCertificate</a>" : <i>[ &lt;a href=&#34;radiusserver-clientrootcertificate.md&#34;&gt;ClientRootCertificate&lt;/a&gt;, ... ]</i>,
    "<a href="#serverrootcertificate" title="ServerRootCertificate">ServerRootCertificate</a>" : <i>[ &lt;a href=&#34;radiusserver-serverrootcertificate.md&#34;&gt;ServerRootCertificate&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#address" title="Address">Address</a>: <i>String</i>
<a href="#secret" title="Secret">Secret</a>: <i>String</i>
<a href="#clientrootcertificate" title="ClientRootCertificate">ClientRootCertificate</a>: <i>
      - &lt;a href=&#34;radiusserver-clientrootcertificate.md&#34;&gt;ClientRootCertificate&lt;/a&gt;</i>
<a href="#serverrootcertificate" title="ServerRootCertificate">ServerRootCertificate</a>: <i>
      - &lt;a href=&#34;radiusserver-serverrootcertificate.md&#34;&gt;ServerRootCertificate&lt;/a&gt;</i>
</pre>

## Properties

#### Address

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Secret

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientRootCertificate

_Required_: No
_Type_: List of &lt;a href=&#34;radiusserver-clientrootcertificate.md&#34;&gt;ClientRootCertificate&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerRootCertificate

_Required_: No
_Type_: List of &lt;a href=&#34;radiusserver-serverrootcertificate.md&#34;&gt;ServerRootCertificate&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

