# Terraform::AzureRM::ServiceFabricCluster CertificateCommonNames

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#x509storename" title="X509StoreName">X509StoreName</a>" : <i>String</i>,
    "<a href="#commonnames" title="CommonNames">CommonNames</a>" : <i>[ &lt;a href=&#34;certificatecommonnames-commonnames.md&#34;&gt;CommonNames&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#x509storename" title="X509StoreName">X509StoreName</a>: <i>String</i>
<a href="#commonnames" title="CommonNames">CommonNames</a>: <i>
      - &lt;a href=&#34;certificatecommonnames-commonnames.md&#34;&gt;CommonNames&lt;/a&gt;</i>
</pre>

## Properties

#### X509StoreName

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CommonNames

_Required_: No
_Type_: List of &lt;a href=&#34;certificatecommonnames-commonnames.md&#34;&gt;CommonNames&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

