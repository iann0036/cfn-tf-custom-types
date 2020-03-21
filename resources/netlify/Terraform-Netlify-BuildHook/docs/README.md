# Terraform::Netlify::BuildHook

Manages build hooks, also known as [incoming webhooks]
(https://www.netlify.com/docs/webhooks/#outgoing-webhooks). These can,
at the time of writing, only be used to trigger new builds of the site.
To create one, provide your site id along with the name of the hook, and
the branch to be built when the hook is triggered.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Netlify::BuildHook",
    "Properties" : {
        "<a href="#branch" title="Branch">Branch</a>" : <i>String</i>,
        "<a href="#siteid" title="SiteId">SiteId</a>" : <i>String</i>,
        "<a href="#title" title="Title">Title</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Netlify::BuildHook
Properties:
    <a href="#branch" title="Branch">Branch</a>: <i>String</i>
    <a href="#siteid" title="SiteId">SiteId</a>: <i>String</i>
    <a href="#title" title="Title">Title</a>: <i>String</i>
</pre>

## Properties

#### Branch

branch to be built when the hook is triggered.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SiteId

Your netlify site's unique id.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Title

name of the webhook - this is purely for organization and
can be any name you want.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Url

Returns the <code>Url</code> value.

