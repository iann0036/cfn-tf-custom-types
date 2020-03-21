# Terraform::Netlify::Site

Primary settings for a Netlify site - should contain the bulk of your configuration. Allows configuration of most aspects of your Netlify site.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Netlify::Site",
    "Properties" : {
        "<a href="#accountslug" title="AccountSlug">AccountSlug</a>" : <i>String</i>,
        "<a href="#customdomain" title="CustomDomain">CustomDomain</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#repo" title="Repo">Repo</a>" : <i>[ <a href="repo.md">Repo</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Netlify::Site
Properties:
    <a href="#accountslug" title="AccountSlug">AccountSlug</a>: <i>String</i>
    <a href="#customdomain" title="CustomDomain">CustomDomain</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#repo" title="Repo">Repo</a>: <i>
      - <a href="repo.md">Repo</a></i>
</pre>

## Properties

#### AccountSlug

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomDomain

(Optional) - Custom domain of the site, must be configured using a CNAME in accordance with [Netlify's docs](https://www.netlify.com/docs/custom-domains). (e.g. `www.example.com`).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

(Required) - Name of your site on Netlify (e.g. **mysite**.netlify.com).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Repo

_Required_: No

_Type_: List of <a href="repo.md">Repo</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### AccountName

Returns the <code>AccountName</code> value.

#### DeployUrl

(Optional).

