# Terraform::Vault::JwtAuthBackend Tune

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#allowedresponseheaders" title="AllowedResponseHeaders">AllowedResponseHeaders</a>" : <i>[ String, ... ]</i>,
    "<a href="#auditnonhmacrequestkeys" title="AuditNonHmacRequestKeys">AuditNonHmacRequestKeys</a>" : <i>[ String, ... ]</i>,
    "<a href="#auditnonhmacresponsekeys" title="AuditNonHmacResponseKeys">AuditNonHmacResponseKeys</a>" : <i>[ String, ... ]</i>,
    "<a href="#defaultleasettl" title="DefaultLeaseTtl">DefaultLeaseTtl</a>" : <i>String</i>,
    "<a href="#listingvisibility" title="ListingVisibility">ListingVisibility</a>" : <i>String</i>,
    "<a href="#maxleasettl" title="MaxLeaseTtl">MaxLeaseTtl</a>" : <i>String</i>,
    "<a href="#passthroughrequestheaders" title="PassthroughRequestHeaders">PassthroughRequestHeaders</a>" : <i>[ String, ... ]</i>,
    "<a href="#tokentype" title="TokenType">TokenType</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#allowedresponseheaders" title="AllowedResponseHeaders">AllowedResponseHeaders</a>: <i>
      - String</i>
<a href="#auditnonhmacrequestkeys" title="AuditNonHmacRequestKeys">AuditNonHmacRequestKeys</a>: <i>
      - String</i>
<a href="#auditnonhmacresponsekeys" title="AuditNonHmacResponseKeys">AuditNonHmacResponseKeys</a>: <i>
      - String</i>
<a href="#defaultleasettl" title="DefaultLeaseTtl">DefaultLeaseTtl</a>: <i>String</i>
<a href="#listingvisibility" title="ListingVisibility">ListingVisibility</a>: <i>String</i>
<a href="#maxleasettl" title="MaxLeaseTtl">MaxLeaseTtl</a>: <i>String</i>
<a href="#passthroughrequestheaders" title="PassthroughRequestHeaders">PassthroughRequestHeaders</a>: <i>
      - String</i>
<a href="#tokentype" title="TokenType">TokenType</a>: <i>String</i>
</pre>

## Properties

#### AllowedResponseHeaders

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuditNonHmacRequestKeys

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuditNonHmacResponseKeys

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultLeaseTtl

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ListingVisibility

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxLeaseTtl

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PassthroughRequestHeaders

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TokenType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

