# Terraform::AWS::AcmpcaCertificateAuthority

CloudFormation equivalent of aws_acmpca_certificate_authority

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::AcmpcaCertificateAuthority",
    "Properties" : {
        "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#permanentdeletiontimeindays" title="PermanentDeletionTimeInDays">PermanentDeletionTimeInDays</a>" : <i>Double</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;, ... ]</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>,
        "<a href="#certificateauthorityconfiguration" title="CertificateAuthorityConfiguration">CertificateAuthorityConfiguration</a>" : <i>[ &lt;a href=&#34;certificateauthorityconfiguration.md&#34;&gt;CertificateAuthorityConfiguration&lt;/a&gt;, ... ]</i>,
        "<a href="#revocationconfiguration" title="RevocationConfiguration">RevocationConfiguration</a>" : <i>[ &lt;a href=&#34;revocationconfiguration.md&#34;&gt;RevocationConfiguration&lt;/a&gt;, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>,
        "<a href="#subject" title="Subject">Subject</a>" : <i>[ &lt;a href=&#34;subject.md&#34;&gt;Subject&lt;/a&gt;, ... ]</i>,
        "<a href="#crlconfiguration" title="CrlConfiguration">CrlConfiguration</a>" : <i>[ &lt;a href=&#34;crlconfiguration.md&#34;&gt;CrlConfiguration&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::AcmpcaCertificateAuthority
Properties:
    <a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#permanentdeletiontimeindays" title="PermanentDeletionTimeInDays">PermanentDeletionTimeInDays</a>: <i>Double</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
    <a href="#certificateauthorityconfiguration" title="CertificateAuthorityConfiguration">CertificateAuthorityConfiguration</a>: <i>
      - &lt;a href=&#34;certificateauthorityconfiguration.md&#34;&gt;CertificateAuthorityConfiguration&lt;/a&gt;</i>
    <a href="#revocationconfiguration" title="RevocationConfiguration">RevocationConfiguration</a>: <i>
      - &lt;a href=&#34;revocationconfiguration.md&#34;&gt;RevocationConfiguration&lt;/a&gt;</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>
    <a href="#subject" title="Subject">Subject</a>: <i>
      - &lt;a href=&#34;subject.md&#34;&gt;Subject&lt;/a&gt;</i>
    <a href="#crlconfiguration" title="CrlConfiguration">CrlConfiguration</a>: <i>
      - &lt;a href=&#34;crlconfiguration.md&#34;&gt;CrlConfiguration&lt;/a&gt;</i>
</pre>

## Properties

#### Enabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PermanentDeletionTimeInDays

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CertificateAuthorityConfiguration

_Required_: No

_Type_: List of &lt;a href=&#34;certificateauthorityconfiguration.md&#34;&gt;CertificateAuthorityConfiguration&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RevocationConfiguration

_Required_: No

_Type_: List of &lt;a href=&#34;revocationconfiguration.md&#34;&gt;RevocationConfiguration&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: &lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Subject

_Required_: No

_Type_: List of &lt;a href=&#34;subject.md&#34;&gt;Subject&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CrlConfiguration

_Required_: No

_Type_: List of &lt;a href=&#34;crlconfiguration.md&#34;&gt;CrlConfiguration&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Arn

Returns the &lt;code&gt;Arn&lt;/code&gt; value.

#### Certificate

Returns the &lt;code&gt;Certificate&lt;/code&gt; value.

#### CertificateChain

Returns the &lt;code&gt;CertificateChain&lt;/code&gt; value.

#### CertificateSigningRequest

Returns the &lt;code&gt;CertificateSigningRequest&lt;/code&gt; value.

#### NotAfter

Returns the &lt;code&gt;NotAfter&lt;/code&gt; value.

#### NotBefore

Returns the &lt;code&gt;NotBefore&lt;/code&gt; value.

#### Serial

Returns the &lt;code&gt;Serial&lt;/code&gt; value.

#### Status

Returns the &lt;code&gt;Status&lt;/code&gt; value.

