# TF::SDM::Resource HttpAuthDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#authheader" title="AuthHeader">AuthHeader</a>" : <i>String</i>,
    "<a href="#defaultpath" title="DefaultPath">DefaultPath</a>" : <i>String</i>,
    "<a href="#egressfilter" title="EgressFilter">EgressFilter</a>" : <i>String</i>,
    "<a href="#headersblacklist" title="HeadersBlacklist">HeadersBlacklist</a>" : <i>String</i>,
    "<a href="#healthcheckpath" title="HealthcheckPath">HealthcheckPath</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#secretstoreauthheaderkey" title="SecretStoreAuthHeaderKey">SecretStoreAuthHeaderKey</a>" : <i>String</i>,
    "<a href="#secretstoreauthheaderpath" title="SecretStoreAuthHeaderPath">SecretStoreAuthHeaderPath</a>" : <i>String</i>,
    "<a href="#secretstoreid" title="SecretStoreId">SecretStoreId</a>" : <i>String</i>,
    "<a href="#subdomain" title="Subdomain">Subdomain</a>" : <i>String</i>,
    "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
    "<a href="#url" title="Url">Url</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#authheader" title="AuthHeader">AuthHeader</a>: <i>String</i>
<a href="#defaultpath" title="DefaultPath">DefaultPath</a>: <i>String</i>
<a href="#egressfilter" title="EgressFilter">EgressFilter</a>: <i>String</i>
<a href="#headersblacklist" title="HeadersBlacklist">HeadersBlacklist</a>: <i>String</i>
<a href="#healthcheckpath" title="HealthcheckPath">HealthcheckPath</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#secretstoreauthheaderkey" title="SecretStoreAuthHeaderKey">SecretStoreAuthHeaderKey</a>: <i>String</i>
<a href="#secretstoreauthheaderpath" title="SecretStoreAuthHeaderPath">SecretStoreAuthHeaderPath</a>: <i>String</i>
<a href="#secretstoreid" title="SecretStoreId">SecretStoreId</a>: <i>String</i>
<a href="#subdomain" title="Subdomain">Subdomain</a>: <i>String</i>
<a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
<a href="#url" title="Url">Url</a>: <i>String</i>
</pre>

## Properties

#### AuthHeader

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultPath

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EgressFilter

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HeadersBlacklist

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthcheckPath

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecretStoreAuthHeaderKey

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecretStoreAuthHeaderPath

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecretStoreId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Subdomain

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Url

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

