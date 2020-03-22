# Terraform::BIGIP::LtmProfileHttpcompress

`bigip_ltm_profile_httpcompress`  Virtual server HTTP compression profile configuration


For resources should be named with their "full path". The full path is the combination of the partition + name of the resource. For example /Common/my-pool.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::BIGIP::LtmProfileHttpcompress",
    "Properties" : {
        "<a href="#contenttypeexclude" title="ContentTypeExclude">ContentTypeExclude</a>" : <i>[ String, ... ]</i>,
        "<a href="#contenttypeinclude" title="ContentTypeInclude">ContentTypeInclude</a>" : <i>[ String, ... ]</i>,
        "<a href="#defaultsfrom" title="DefaultsFrom">DefaultsFrom</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#uriexclude" title="UriExclude">UriExclude</a>" : <i>[ String, ... ]</i>,
        "<a href="#uriinclude" title="UriInclude">UriInclude</a>" : <i>[ String, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::BIGIP::LtmProfileHttpcompress
Properties:
    <a href="#contenttypeexclude" title="ContentTypeExclude">ContentTypeExclude</a>: <i>
      - String</i>
    <a href="#contenttypeinclude" title="ContentTypeInclude">ContentTypeInclude</a>: <i>
      - String</i>
    <a href="#defaultsfrom" title="DefaultsFrom">DefaultsFrom</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#uriexclude" title="UriExclude">UriExclude</a>: <i>
      - String</i>
    <a href="#uriinclude" title="UriInclude">UriInclude</a>: <i>
      - String</i>
</pre>

## Properties

#### ContentTypeExclude

Excludes a specified list of content types from compression of HTTP Content-Type responses. Use a string list to specify a list of content types you want to compress.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ContentTypeInclude

Specifies a list of content types for compression of HTTP Content-Type responses. Use a string list to specify a list of content types you want to compress.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultsFrom

Specifies the profile that you want to use as the parent profile. Your new profile inherits all settings and values from the parent profile specified.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UriExclude

Disables compression on a specified list of HTTP Request-URI responses. Use a regular expression to specify a list of URIs you do not want to compress.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UriInclude

Enables compression on a specified list of HTTP Request-URI responses. Use a regular expression to specify a list of URIs you want to compress.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

