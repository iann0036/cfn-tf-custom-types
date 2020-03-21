# Terraform::OpenStack::IdentityApplicationCredentialV3 AccessRules

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#method" title="Method">Method</a>" : <i>String</i>,
    "<a href="#path" title="Path">Path</a>" : <i>String</i>,
    "<a href="#service" title="Service">Service</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#method" title="Method">Method</a>: <i>String</i>
<a href="#path" title="Path">Path</a>: <i>String</i>
<a href="#service" title="Service">Service</a>: <i>String</i>
</pre>

## Properties

#### Method

The request method that the application credential is
permitted to use for a given API endpoint. Allowed values: `POST`, `GET`,
`HEAD`, `PATCH`, `PUT` and `DELETE`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Path

The API path that the application credential is permitted
to access. May use named wildcards such as **{tag}** or the unnamed wildcard
**\*** to match against any string in the path up to a **/**, or the recursive
wildcard **\*\*** to include **/** in the matched path.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Service

The service type identifier for the service that the
application credential is granted to access. Must be a service type that is
listed in the service catalog and not a code name for a service. E.g.
**identity**, **compute**, **volumev3**, **image**, **network**,
**object-store**, **sharev2**, **dns**, **key-manager**, **monitoring**, etc.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

