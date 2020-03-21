# Terraform::AzureAD::ServicePrincipalPassword

Manages a Password associated with a Service Principal within Azure Active Directory.

-> **NOTE:** If you're authenticating using a Service Principal then it must have permissions to both `Read and write all applications` and `Sign in and read user profile` within the `Windows Azure Active Directory` API.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AzureAD::ServicePrincipalPassword",
    "Properties" : {
        "<a href="#enddate" title="EndDate">EndDate</a>" : <i>String</i>,
        "<a href="#enddaterelative" title="EndDateRelative">EndDateRelative</a>" : <i>String</i>,
        "<a href="#keyid" title="KeyId">KeyId</a>" : <i>String</i>,
        "<a href="#serviceprincipalid" title="ServicePrincipalId">ServicePrincipalId</a>" : <i>String</i>,
        "<a href="#startdate" title="StartDate">StartDate</a>" : <i>String</i>,
        "<a href="#value" title="Value">Value</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AzureAD::ServicePrincipalPassword
Properties:
    <a href="#enddate" title="EndDate">EndDate</a>: <i>String</i>
    <a href="#enddaterelative" title="EndDateRelative">EndDateRelative</a>: <i>String</i>
    <a href="#keyid" title="KeyId">KeyId</a>: <i>String</i>
    <a href="#serviceprincipalid" title="ServicePrincipalId">ServicePrincipalId</a>: <i>String</i>
    <a href="#startdate" title="StartDate">StartDate</a>: <i>String</i>
    <a href="#value" title="Value">Value</a>: <i>String</i>
</pre>

## Properties

#### EndDate

The End Date which the Password is valid until, formatted as a RFC3339 date string (e.g. `2018-01-01T01:02:03Z`). Changing this field forces a new resource to be created.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EndDateRelative

A relative duration for which the Password is valid until, for example `240h` (10 days) or `2400h30m`. Valid time units are "ns", "us" (or "µs"), "ms", "s", "m", "h". Changing this field forces a new resource to be created.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeyId

A GUID used to uniquely identify this Key. If not specified a GUID will be created. Changing this field forces a new resource to be created.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServicePrincipalId

The ID of the Service Principal for which this password should be created. Changing this field forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StartDate

The Start Date which the Password is valid from, formatted as a RFC3339 date string (e.g. `2018-01-01T01:02:03Z`). If this isn't specified, the current date is used.  Changing this field forces a new resource to be created.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Value

The Password for this Service Principal.

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

